#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Creates a LIFO cache system"""
    def __init__(self):
        """Invokes base class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Assigns key to item in cache system"""
        d_cache = self.cache_data
        if key and item:
            if key in self.cache_data.keys():
                return
            elif len(d_cache) >= BaseCaching.MAX_ITEMS:
                # discard last item added
                pop_k, pop_v = d_cache.popitem()
                print(f"DISCARD: {pop_k}")
            d_cache[key] = item

    def get(self, key):
        """Retrieve item from cache"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
