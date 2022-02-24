class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        K = 2
        len_p = len(prices)
        # 定义三维dp数组  dp[i][k][0] 和 dp[i][k][1]
        dp = [[[0, 0] for _ in range(K+1)] for _ in range(len_p)]
        for i in range(len_p):
            for k in range(1, K+1):
                # base case
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[len_p-1][K][0]

    def maxProfit2(self, prices):
        len_p = len(prices)
        # base case
        dp_i_10 = 0  # dp[0][0][0]
        dp_i_11 = -prices[0]  # dp[0][1][1]
        dp_i_20 = 0  # dp[0][2][0]
        dp_i_21 = -prices[0]  # dp[0][2][1]
        for i in range(len_p):
            dp_i_10 = max(dp_i_10, dp_i_11+prices[i])
            dp_i_11 = max(dp_i_11, -prices[i])   # max(dp_i_11, dp_i_00-prices[i])
            dp_i_20 = max(dp_i_20, dp_i_21+prices[i])
            dp_i_21 = max(dp_i_21, dp_i_10-prices[i])
        return dp_i_20
if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices1 = [1, 2, 3, 4, 5]
    rel = Solution().maxProfit1(prices)
    print(rel)
