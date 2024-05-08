#!/usr/bin/env python3
"""
BasicCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class

    - use self.cache_data dictionary from parent class
    - the caching system doesn't have a limit

    Methods:
    - put(key, item): assigning item to the value for the key in the
    cache_data dictionary
    If key or item is None, this method should not do anything

    - get(key): return the value in cache_data linked to key
    If key is None or if the key doesn't exist in cache_data, return None
    """

    def put(self, key, item):
        """
        Assigning item to the value for the key in the
        cache_data dictionary

        If key or item is None, this method should not do anything
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in cache_data linked to key

        If key is None or if the key doesn't exist in cache_data,
        return None
        """
        if (key is None):
            return None

        return self.cache_data.get(key)
