#!/usr/bin/env python3
"""
LFUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache Class

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
        self.cache_usage = {}

    def put(self, key, item):
        """
        Assigning item to the value for the key in the
        cache_data dictionary

        * If key or item is None, this method should not do anything
        * If the number of items in self.cache_data is higher than
        MAX_ITEMS:
            - discard the least frequency used item in cache (LFU algorithm)
            - if more than 1 item to discard, use LRU algorithm to discard
            - print DISCARD: with the key discarded and followed by a
              new line
        """
        if (key is not None and item is not None):

            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = None
                min_val = min([x for x in self.cache_usage.values()])
                for c_key, c_val in self.cache_data.items():
                    key_min = self.cache_usage.get(c_key)
                    if key_min == min_val:
                        lfu_key = c_key
                        break
                print("DISCARD: {}".format(lfu_key))
                self.cache_data.pop(lfu_key)
                self.cache_usage.pop(lfu_key)

            self.cache_data[key] = item
            if self.cache_usage.get(key) is not None:
                self.cache_usage[key] = self.cache_usage.get(key) + 1
            else:
                self.cache_usage[key] = 1

    def get(self, key):
        """
        Return the value in cache_data linked to key

        If key is None or if the key doesn't exist in cache_data,
        return None
        """
        if (key is None or key not in self.cache_data):
            return None

        value = self.cache_data.get(key)

        if self.cache_usage.get(key) is not None:
            self.cache_usage[key] = self.cache_usage.get(key) + 1

        return value
