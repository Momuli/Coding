class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        digit = 1
        low = 0
        high = n // 10
        cur = n % 10
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low = cur * digit + low
            cur = high % 10
            high = high // 10
            digit = digit * 10
        return res

if __name__ == '__main__':
    n = 13
    rel = Solution().countDigitOne(n)
    print(rel)