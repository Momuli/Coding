class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n & 1:
                res += 1
            n = n >> 1   # 将n的二进制右移一位
        return res

    def hammingWeight2(self, n):
        s = bin(n)[2:]   # n的二进制表示0b...
        return s.count('1')
