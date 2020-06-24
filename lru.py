"""
Leet Code Problem 146 - LRU Cache
"""
from collections import OrderedDict


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    def __repr__(self):
        return str(self.cache)
        
    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
            return
        self.cache[key] = value
