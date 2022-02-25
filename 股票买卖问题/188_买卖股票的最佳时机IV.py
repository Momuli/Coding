class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][0 or 1]
        len_p = len(prices)
        # 定义三维dp数组
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(len_p)]
        for i in range(len_p):
            for j in range(1, k+1):
                # base case
                if i-1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

            return dp[len_p-1][k][0] if len_p else 0
if __name__ == '__main__':
    # prices = [2, 4, 1]
    # k = 2
    k = 2
    # prices = [3, 2, 6, 5, 0, 3]
    prices = []
    rel = Solution().maxProfit(k, prices)
    print(rel)