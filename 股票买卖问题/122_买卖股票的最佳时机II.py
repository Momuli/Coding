class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_p = len(prices)
        # 定义dp数组
        dp = [[0, 0] for _ in range(len_p)]
        # base case
        dp[0][0] = 0
        dp[0][1] = -prices[0]  # 第0天买入股票,但不在有交易次数限制
        # 状态转移
        for i in range(1, len_p):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[len_p-1][0]

    def maxProfit2(self, prices):
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, temp-prices[i])
        return dp_i_0

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    rel = Solution().maxProfit2(prices)
    print(rel)

