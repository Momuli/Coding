class Solution(object):
    def maxProfit1(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        len_p = len(prices)
        dp = [[0, 0] for _ in range(len_p)]
        for i in range(len_p):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]-fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[len_p - 1][0]

    def maxProfit2(self, prices, fee):
        len_p = len(prices)
        dp_i_00 = 0
        dp_i_01 = -prices[0] - fee
        for i in range(len_p):
            dp_i_00 = max(dp_i_00, dp_i_01+prices[i])
            dp_i_01 = max(dp_i_01, dp_i_00-prices[i]-fee)
        return dp_i_00

if __name__ == '__main__':
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        rel = Solution().maxProfit2(prices, fee)
        print(rel)

