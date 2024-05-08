#!/usr/bin/env python3
"""
MRUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache Class

    - use self.cache_data dictionary from parent class
    - the caching system has a limit of BaseCaching.MAX_ITEMS

    Methods:
    - put(key, item): assigning item to the value for the key in the
    cache_data dictionary

    - get(key): return the value in cache_data linked to key
    """
    def __init__(self):
        """
        Initialise
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigning item to the value for the key in the
        cache_data dictionary

        * If key or item is None, this method should not do anything
        * If the number of items in self.cache_data is higher than
        MAX_ITEMS:
            - discard the most recently used item put in cache (MRU algorithm)
            - print DISCARD: with the key discarded and followed by a
              new line
        """
        if (key is not None and item is not None):

            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                print("DISCARD: {}".format(mru_key))
                self.cache_data.pop(mru_key)

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in cache_data linked to key

        If key is None or if the key doesn't exist in cache_data,
        return None
        """
        if (key is None or key not in self.cache_data):
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
