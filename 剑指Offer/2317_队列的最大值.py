import collections
class MaxQueue(object):
    def __init__(self):
        self.queue1 = collections.deque()   # 正常顺序存储元素
        self.queue2 = collections.deque()   # 元素大小顺序排放元素
    def max_value(self):
        """
        :rtype: int
        """
        if not self.queue1:
            return -1
        else:
            return self.queue2[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 弹出queue2中比当前需要添加的value小的元素
        while self.queue2 and self.queue2[-1] < value:
            self.queue2.pop()
        self.queue2.append(value)
        self.queue1.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue1:
            return -1
        else:
            ans = self.queue1[0]
            if ans == self.queue2[0]:
                self.queue2.popleft()
            return self.queue1.popleft()




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()