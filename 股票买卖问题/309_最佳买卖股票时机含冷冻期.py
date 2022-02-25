class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0]-prices[i])
        # k为无限次,因此可以直接拿掉
        len_p = len(prices)
        dp = [[0, 0] for _ in range(len_p)]
        for i in range(len_p):
            # base case 1
            if i-1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            # 当i=1是,dp[1][1]:若要第一天持有股票,那么第0天就持有股票或者 第0天不持股票且没有买过股票,第1天再买股票
            if i-2 == -1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[len_p-1][0]
    # 空间优化
    def maxProfit2(self, prices):
        len_p = len(prices)
        dp_i_00 = 0
        dp_i_01 = -prices[0]
        dp_i_pre = 0
        for i in range(len_p):
            temp = dp_i_00
            dp_i_00 = max(dp_i_00, dp_i_01+prices[i])
            dp_i_01 = max(dp_i_01, dp_i_pre-prices[i])
            dp_i_pre = temp    # 因为要冻结一天,因此dp[i][1]中的dp[i-2][0]要是前两天的状态
        return dp_i_00

if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    rel = Solution().maxProfit2(prices)
    print(rel)
