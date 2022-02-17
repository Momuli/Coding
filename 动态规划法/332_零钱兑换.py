class Solution(object):
    # 自底向上的迭代
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)   # 初始化dp[i]为最大值
        dp[0] = 0   # base case

        for i in range(1, amount+1):
            for item in coins:
                retain = i - item    # 当前目标面额-面币值
                if retain >= 0:
                    dp[i] = min(dp[i], dp[retain]+1)

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]

    # 暴力递归(存在重叠子问题的重复计算)
    def coinChange2(self, coins, amount):
        if amount == 0:     # base case
            return 0
        if amount < 0:    # amount:3   面币金额:5
            return -1

        res = amount + 3   # res是一个尽可能大的数
        for item in coins:
            sub_rel = self.coinChange2(coins, amount-item)
            if sub_rel == -1:    # 当前子问题无解(凑不出)
                continue
            res = min(res, sub_rel+1)

        if res == amount + 3:
            return -1
        else:
            return res

    # 带备忘录的递归
    memo = []
    def coinChange3(self, coins, amount):
        for i in range(amount+1):
            self.memo.append(-666)
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = amount + 3
        for item in coins:
            sub_rel = self.coinChange3(coins, amount-item)
            if sub_rel == -1:
                continue
            res = min(res, sub_rel+1)

        if res != amount + 3:
            self.memo[amount] = res
        else:
            self.memo[amount] = -1

        return self.memo[amount]



if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    rel = Solution().coinChange3(coins, amount)
    print(rel)

