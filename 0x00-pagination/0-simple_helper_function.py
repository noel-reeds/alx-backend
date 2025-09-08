#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple corr. to pagination params"""
    end = page * page_size
    if page < 1:
        start = 0
    else:
        start = end - page_size
    return (start, end)
