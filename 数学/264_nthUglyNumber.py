class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        p2 = 1
        p3 = 1
        p5 = 1
        i = 1
        while i < n:
            i += 1
            dp.append(min(dp[p2]*2, dp[p3]*3, dp[p5]*5))
            if dp[i] == dp[p2]*2:
                p2 += 1
            if dp[i] == dp[p3]*3:
                p3 += 1
            if dp[i] == dp[p5]*5:
                p5 += 1
        return dp[i]

if __name__ == '__main__':
    n = 10
    rel = Solution().nthUglyNumber(n)
    print(rel)