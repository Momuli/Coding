class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r

    def climbStairs2(self, n):
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

    def climbStairs3(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            rel = Solution().climbStairs3(n-1) + Solution().climbStairs3(n-2)
            return rel

if __name__ == '__main__':
    n = 10
    rel = Solution().climbStairs3(n)
    print(rel)