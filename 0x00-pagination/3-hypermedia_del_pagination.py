#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple corr. to pagination params"""
    end = page * page_size
    if page < 1:
        start = 0
    else:
        start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        lst = self.dataset()
        start, end = index_range(page, page_size)
        if end > (ln_lst := len(lst)):
            return []
        return lst[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Hypermedia pagination"""
        ln_lst = len(self.dataset())
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if ln_lst >= page * page_size else None,
            'prev_page': None if page == 1 else page - 1,
            'total_pages': ln_lst
            }

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """deletion-resilient hypermedia pagination"""
        d_lst = self.dataset()
        assert index in self.indexed_dataset().keys()
        items_from_0 = index + page_size
        page = items_from_0 / page_size
        return {
            'index': index,
            'next_index': index + page_size,
            'page_size': page_size,
            'data': [d_lst[i] for i in range(index, index + page_size)]
        }
