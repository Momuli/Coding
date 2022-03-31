from collections import OrderedDict
class Solution:
    def __init__(self, capacity: int):
        # write code here
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key: int) -> int:
        # write code here
        if not self.cache:
            return -1
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def set(self, key: int, value: int) -> None:
        # write code here
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)