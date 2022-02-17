class CQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack_in.extend([value])   # 直接将元素插入入栈即可

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack_out:   # 如果出栈为空
            if not self.stack_in:
                return -1
            else:
                while self.stack_in:
                    self.stack_out.extend([self.stack_in.pop()])
                return self.stack_out.pop()
        else:
            return self.stack_out.pop()







# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()