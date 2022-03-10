class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        half = self.myPow(x, n // 2)
        # n为奇数
        if n & 1:
            return half * half * x
        else:
            return half * half

if __name__ == '__main__':
    x = 2.000
    n = -3
    rel = Solution().myPow(x, n)
    print(rel)
