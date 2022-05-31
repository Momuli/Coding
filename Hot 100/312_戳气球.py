# 动态规划
# 先给数组的收尾添加元素1
# dp[i][j]表示戳破开区间(i,j)之间的所有气球，可以获得的最大分数
# 最终的答案为dp[0][n+1]
# 对于区间(i,j):需要选择区间内最后一个戳破的气球k
# i:从下往上遍历,其实元素就是nums的最后一个元素的位置
# j:从左向右遍历,一定比i大
class Solution:
    def maxCoins(self, nums):
        # 给 nums收尾添加1
        temp = [0] * (len(nums) + 2)
        temp[0] = 1
        temp[-1] = 1
        for i in range(1, len(temp) - 1):
            temp[i] = nums[i - 1]
        # dp[i][j]表示戳破开区间（i,j）子数组中的所有气球，可以获得的最大分数
        dp = [[0 for _ in range(len(temp))] for _ in range(len(temp))]
        # i 从下往上
        for i in range(len(nums), -1, -1):
            # j 从左向右
            for j in range(i + 1, len(temp)):
                # 选择最后戳破的气球
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + temp[i] * temp[k] * temp[j])
        return dp[0][-1]
