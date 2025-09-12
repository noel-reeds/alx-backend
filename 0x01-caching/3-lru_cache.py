#!/usr/bin/env python3
"""LRU Caching"""
from collections import defaultdict
from functools import wraps
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements a Least Recently Used algorithm"""
    def __init__(self):
        """Invoke base class init method"""
        BaseCaching.__init__(self)
        self.lru_counter = defaultdict(int)

    def put(self, key, item):
        """Assigns key to item in cache"""
        d_cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                d_cache[key] = item
                return
            counter = self.lru_counter
            if len(d_cache) >= BaseCaching.MAX_ITEMS:
                # discard the least recently used - lru
                lru_k = list(counter)[0]
                lru_v = counter.get(lru_k)
                for k in counter.keys():
                    v = counter.get(k)
                    if v < lru_v:
                        lru_v = v
                        lru_k = k
                # update counter & cache
                counter.pop(lru_k)
                d_cache.pop(lru_k)
                print(f"DISCARD: {lru_k}")
            d_cache[key] = item
            counter[key] = 0

    def counted(fn):
        """Keeps track of get fn calls"""
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            key = args[0]
            if key in self.cache_data.keys():
                self.lru_counter[key] += 1
            return fn(self, *args, **kwargs)
        return wrapper

    @counted
    def get(self, key):
        """return the value linked to key"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
