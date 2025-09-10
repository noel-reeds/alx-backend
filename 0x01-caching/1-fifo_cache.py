#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """Creates a basic FIFO caching system"""
    def __init__(self):
        """Invokes base class init method"""
        super().__init__()

    def put(self, key, item):
        """Assigns item to a key in cached data"""
        d_cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                return
            elif len(d_cache) >= BaseCaching.MAX_ITEMS:
                first_in = list(d_cache)[0]
                # discard first item added
                value = d_cache.pop(first_in)
                print(f"DISCARD: {first_in}")
            d_cache[key] = item

    def get(self, key):
        """Retrieve a key from cache"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
