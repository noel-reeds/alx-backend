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

    def put(self, key, item):
        """Assigns key to item in cache"""
        d_cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                return
            elif len(d_cache) >= BaseCaching.MAX_ITEMS:
                # discard the least recently used - lru
                counter = self.lru_counter
                lru_k = list(counter)[0]
                lru_v = counter.get(lru_k)
                for k in counter.keys():
                    if (v := counter.get(k)) < lru_v:
                        lru_v = v
                        lru_k = k
                # update counter & cache
                counter.pop(lru_k)
                d_cache.pop(lru_k)
                print(f"DISCARD: {lru_k}")
            d_cache[key] = item

    def counted(fn):
        """Keeps track of get fn calls"""
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            if (lru_counter := getattr(self, 'lru_counter', None)) is None:
                self.lru_counter = defaultdict(int)
            key = args[0]
            self.lru_counter[key] += 1
            return fn(self, *args, **kwargs)
        return wrapper

    @counted
    def get(self, key):
        """return the value linked to key"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
