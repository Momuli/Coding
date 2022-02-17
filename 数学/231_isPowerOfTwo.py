class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        else:
            return Solution().isPowerOfTwo(n // 2)

if __name__ == '__main__':
    n = 64
    rel = Solution().isPowerOfTwo(n)
    print(rel)
