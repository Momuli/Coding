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
        dp[0][0] = 0  # 第0天,不持有股票
        dp[0][1] = -prices[0]  # 第0天,买入股票
        # 状态转移
        for i in range(1, len_p):
            # 第i天不持有股票的最大利润:max(第i-1天不持有股票的最大利润, 第i-1天持有股票但在第i天卖出后的最大利润)
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 第i天持有股票的最大利润:max(第i-1天持有股票的最大利润, 第i-1天不持有股票但在第i天买入股票后的最大利润)
            dp[i][1] = max(dp[i-1][1], -prices[i])   # dp[i-1][0] = 0
        return dp[len_p-1][0]

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_p = len(prices)
        # base case
        dp_i_0 = 0  # 第0天,不持有股票
        dp_i_1 = -prices[0]  # 第0天,买入股票
        # 状态转移
        for i in range(1, len_p):
            # 第i天不持有股票的最大利润:max(第i-1天不持有股票的最大利润, 第i-1天持有股票但在第i天卖出后的最大利润)
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            # 第i天持有股票的最大利润:max(第i-1天持有股票的最大利润, 第i-1天不持有股票但在第i天买入股票后的最大利润)
            dp_i_1 = max(dp_i_1, -prices[i])   # dp[i-1][0] = 0
        return dp_i_0

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    rel = Solution().maxProfit2(prices)
    print(rel)
