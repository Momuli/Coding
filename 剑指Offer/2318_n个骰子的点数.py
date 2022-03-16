class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        # 初始化dp数组
        dp = [1/6] * 6   # 当只有1个骰子时,取值范围[0,5]
        for i in range(2, n+1):
            temp = [0] * (5 * i + 1)    # 2个骰子时的点数和范围[0, 10],长度为11
            # 每个dp[n-1]的取值对dp[n]的影响     [1+0, 1+1, 1+2, 1+3, 1+4, 1+5]
            for j in range(len(dp)):
                for k in range(6):
                    dp[k+j] += dp[j] / 6
            dp = temp
        return dp