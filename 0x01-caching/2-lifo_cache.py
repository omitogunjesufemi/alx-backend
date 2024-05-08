#!/usr/bin/env python3
"""
LIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache Class

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
        MAX_ITEMS:
            - discard the last item put in cache (LIFO algorithm)
            - print DISCARD: with the key discarded and followed by a
              new line
        """
        if (key is not None and item is not None):
            max_limit = BaseCaching.MAX_ITEMS
            cache_len = len(self.cache_data)

            cache_keys = [x for x in self.cache_data.keys()]

            if cache_len >= max_limit:
                if key in cache_keys:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    discard_key, discard_value = self.cache_data.popitem()
                    print(f"DISCARD: {discard_key}")
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
