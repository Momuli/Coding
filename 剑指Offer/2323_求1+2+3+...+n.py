class Solution(object):
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res