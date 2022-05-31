# 背包问题
# 用完全平方数将容量为n的背包装满，最少需要几个
class Solution:
    def numSquares(self, n):
        # 最坏情况下n用1表示，共需要n个
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]

n = 12
rel = Solution().numSquares(n)
print(rel)
