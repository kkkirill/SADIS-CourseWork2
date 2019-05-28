import os
from pathlib import Path
from pickle import dumps, loads, HIGHEST_PROTOCOL, dump, load
from typing import List
from src.models.accounts import Account
from src.models.feedback import Feedback
from src.models.order import Order


class FileManager:

    def __init__(self):
        pass

    def get_feedbacks(self, path: Path=None) -> List[Feedback]:
        feedbacks = []
        for i, dir in enumerate(os.listdir(path)):
            temppath = path.joinpath(dir, 'feedbacks.txt')
            if os.path.exists(temppath):
                with open(temppath, mode='rb') as f:
                    while True:
                        try:
                            feedback = load(f)
                        except EOFError:
                            break
                        feedbacks.append(feedback)
        # if not os.path.exists(filename):
        #     os.makedirs(filename)
        # filename = filename.joinpath('feedbacks.txt')
        # if os.path.exists(filename):
        #     with open(filename, 'rb') as f:
        return feedbacks

    def write_feedbacks(self, feedbacks: List[Feedback], filename: str=None):
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename = filename.joinpath('feedbacks.txt')
        if os.path.exists(filename):
            with open(filename, mode='w') as f:
                for feedback in feedbacks:
                    dump(feedback, f)

    def append_feedbacks(self, feedback: Feedback, filename: str=None):
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename = filename.joinpath('feedbacks.txt')
        mode = 'ab' if os.path.exists(filename) else 'wb'
        with open(filename, mode=mode) as f:
            dump(feedback, f)

    def get_orders(self, filename: str=None) -> List[Order]:
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename = filename.joinpath('orders.txt')
        orders = []
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                while True:
                    try:
                        order = load(f)
                    except EOFError:
                        break
                    orders.append(order)
        return orders

    def write_orders(self, orders: List[Order], filename: str=None):
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename = filename.joinpath('orders.txt')
        with open(filename, 'wb') as f:
            for order in orders:
                dump(order, f)

    def append_order(self, order: Order, filename: str=None):
        if not os.path.exists(filename):
            os.makedirs(filename)
        filename = filename.joinpath('orders.txt')
        mode = 'wb' if not os.path.exists(filename) else 'ab'
        with open(filename, mode=mode) as f:
            dump(order, f)

    def get_content_from_file(self, filename: str) -> str:
        with open(filename, 'r', encoding='windows-1251') as f:
            f.seek(0)
            if not f.read(1):
                return ''
            else:
                f.seek(0)
                return '|'.join(map(lambda s: s.strip(), f.readlines()))

    def write_to_file(self, content: str, filename: str) -> bool:
        with open(filename, 'w') as f:
            f.write(content)
        return f.closed

    def append_to_file(self, content: str, filename: str) -> bool:
        with open(filename, 'a') as f:
            f.write(content)
        return f.closed