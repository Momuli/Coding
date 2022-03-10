class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        mod = 10**9+7
        res = 1
        # 因为4的时候分解成2*2,乘积最大
        while n > 4:
            res = res * 3     # 总共可以拆多少个3
            res = res % mod
            n = n - 3
        # 此时的n<=4
        return res * n % mod