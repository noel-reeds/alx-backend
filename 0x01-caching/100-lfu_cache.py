#!/usr/bin/env python3
"""LRU Caching"""
from typing import Callable, Union
from collections import defaultdict
from functools import wraps
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Implements a Least Recently Used algorithm"""
    def __init__(self):
        """Invoke base class init method"""
        BaseCaching.__init__(self)
        self.lfu_counter = defaultdict(int)

    def put(self, key: str, item: str) -> None:
        """Assigns key to item in cache"""
        cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                cache[key] = item
                return
            counter = self.lfu_counter
            if len(cache) >= BaseCaching.MAX_ITEMS:
                # discard the least frequently used - lfu
                lfu_k = list(counter)[0]
                lfu_v = counter.get(lfu_k)
                for k in counter.keys():
                    v = counter.get(k)
                    if v < lfu_v:
                        lfu_v = v
                        lfu_k = k
                # update counter & cache
                counter.pop(lfu_k)
                cache.pop(lfu_k)
                print(f"DISCARD: {lfu_k}")
            cache[key] = item
            counter[key] = 0

    def counted(fn: Callable) -> Callable:
        """Keeps track of get fn calls"""
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            key = args[0]
            if key in self.cache_data.keys():
                self.lfu_counter[key] += 1
            return fn(self, *args, **kwargs)
        return wrapper

    @counted
    def get(self, key: str) -> Union[str, None]:
        """return the value linked to key"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
