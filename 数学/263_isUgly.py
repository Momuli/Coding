class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return Solution().isUgly(n // 2)
        elif n % 3 == 0:
            return Solution().isUgly(n // 3)
        elif n % 5 == 0:
            return Solution().isUgly(n // 5)
        else:
            return False

if __name__ == '__main__':
    n = 16
    rel = Solution().isUgly(n)
    print(rel)