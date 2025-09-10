#!/usr/bin/env python3
"""Creates a class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Creates a basic cache in form of a dictionary"""
    def __init__(self):
        """Invoke parent class"""
        super().__init__()

    def put(self, key, item):
        """Assigns value to key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to key"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
