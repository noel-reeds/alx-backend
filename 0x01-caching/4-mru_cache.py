#!/usr/bin/env python3
"""LRU Caching"""
from collections import defaultdict
from functools import wraps
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Implements a Least Recently Used algorithm"""
    def __init__(self):
        """Invoke base class init method"""
        BaseCaching.__init__(self)
        self.mru = None

    def put(self, key, item):
        """Assigns key to item in cache"""
        cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                cache[key] = item
                return
            elif len(cache) >= BaseCaching.MAX_ITEMS:
                # discard the most recently used - mru
                if self.mru in cache.keys():
                    cache.pop(self.mru)
                    print(f"DISCARD: {self.mru}")
                else:
                    # if None, remove first item in cache
                    k, v = cache.popitem()
                    print(f"DISCARD: {k}")
            cache[key] = item

    def counted(fn):
        """Keeps track of get fn calls"""
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            keys = args[0]
            if keys in self.cache_data.keys():
                self.mru = keys
            return fn(self, *args, **kwargs)
        return wrapper

    @counted
    def get(self, key):
        """return the value linked to key"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
