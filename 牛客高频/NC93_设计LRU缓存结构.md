## 模拟题+哈希表！

**思路:**
1. 利用有序字典:`collections.OrderedDict()`
2. 将刚刚使用添加的`key`或者刚刚访问过的`key`移动到字典末尾
3. 当字典长度超出`capacity`时,删除字典的首个元素
4. `dict.move_to_end(key)`:将key移动到字典末尾
5. `dict.popitem(last):`
* 当`last=True`:弹出最后一个元素
* 当`last=False`:弹出首个元素

**代码:**
```
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
```