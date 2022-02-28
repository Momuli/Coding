class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.stack_min:
            # 如果新添加的元素x<stack_min的栈顶元素,则新添加的x作为stack_min的栈顶元素
            if x <= self.stack_min[-1]:
                self.stack_min.append(x)
        else:
            self.stack_min.append(x)
        return

    def pop(self):
        """
        :rtype: None
        """
        rel = self.stack[-1]
        self.stack.pop()
        if self.stack_min:
            if rel == self.stack_min[-1]:
                self.stack_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        # min_stack = sorted(self.stack)
        return self.stack_min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()