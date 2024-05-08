#!/usr/bin/env python3
"""
FIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache Class

    - use self.cache_data dictionary from parent class
    - the caching system has a limit of BaseCaching.MAX_ITEMS

    Methods:
    - put(key, item): assigning item to the value for the key in the
    cache_data dictionary

    - get(key): return the value in cache_data linked to key
    """

    def put(self, key, item):
        """
        Assigning item to the value for the key in the
        cache_data dictionary

        * If key or item is None, this method should not do anything
        * If the number of items in self.cache_data is higher than
        MAX_ITEMS
            - discard the first item put in cache (FIFO algorithm)
            - print DISCARD: with the key discarded and following
              by a new line
        """
        if (key is not None and item is not None):
            max_limit = BaseCaching.MAX_ITEMS
            cache_len = len(self.cache_data)
            self.cache_data[key] = item
            if cache_len >= max_limit:
                cache_keys = [x for x in self.cache_data.keys()]
                discard_key = cache_keys[0]
                self.cache_data.pop(discard_key)
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        Return the value in cache_data linked to key

        If key is None or if the key doesn't exist in cache_data,
        return None
        """
        if (key is None):
            return None

        return self.cache_data.get(key)
