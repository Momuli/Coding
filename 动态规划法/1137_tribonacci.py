class Solution(object):
    def tribonacci1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        rel = Solution().tribonacci1(n-1) + Solution().tribonacci1(n-2) + Solution().tribonacci1(n-3)
        return rel

    def tribonacci2(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        if n > 2:
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

    def tribonacci3(self, n):
        fir = 0
        sec = 1
        thi = 1
        rel = 0
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        while n > 2:
            rel = fir + sec + thi
            fir = sec
            sec = thi
            thi = rel
            n = n - 1
        return rel

if __name__ == '__main__':
        n = 0
        rel = Solution().tribonacci2(n)
        print(rel)