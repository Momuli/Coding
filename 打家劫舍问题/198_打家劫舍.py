class Solution(object):
    # 状态转移方程:
    # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    # = max(前一间房子没有被偷获取的最大金额, 前一间房子被偷后获取的最大金额)

    # dp[i][1] = dp[i - 1][0] + nums[i]
    # = 前一间房子没有被偷获取的最高金额 + 这间房子拥有的金额
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义dp数组
        dp = [[0, 0] for _ in range(len(nums))]
        # base case
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][1] = dp[i-1][0] + nums[i]
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
        return max(dp[len(nums)-1][1], dp[len(nums)-1][0])
    # rob1空间优化版本
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义base case
        dp_i_0 = 0
        dp_i_1 = nums[0]
        for i in range(1, len(nums)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1)
            dp_i_1 = temp + nums[i]
        return max(dp_i_0, dp_i_1)

    # 自顶向下的递归(存在重复计算的子问题)
    # 第i间被抢,那么第i+1间一定不被抢,第i+2间可以选择抢或者不抢
    def rob3(self, nums):
        # 从nums[start]开始抢,可以获得的最大金额
        res = self.max_money1(nums, 0)
        return res

    def max_money1(self, nums, start):
        # base case
        if start >= len(nums):
            return 0
        r = max(self.max_money1(nums, start+1), nums[start]+self.max_money1(nums, start+2))
        return r

    # 加备忘录的递归方法
    def rob4(self, nums):
        # 从nums[start]开始抢,可以获得的最大金额
        self.memo = [-1] * len(nums)
        res = self.max_money2(nums, 0)
        return res

    def max_money2(self, nums, start):
        # base case
        if start >= len(nums):
            return 0
        if self.memo[start] != -1:
            return self.memo[start]
        r = max(self.max_money2(nums, start+1), nums[start]+self.max_money2(nums, start+2))
        self.memo[start] = r
        return r

    # 自底向上
    def rob5(self, nums):
        # 定义dp数组
        # dp[i]:表示从第i间房子开始抢劫,可以获得的最高金额
        dp = [0] * (len(nums) + 2)
        # base case
        dp[-1] = 0
        dp[-2] = 0
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        return dp[0]

    # rob5的空间优化
    def rob6(self, nums):
        dp_i_1 = 0
        dp_i_2 = 0
        re = 0
        for i in range(len(nums)-1, -1, -1):
            re = max(dp_i_1, dp_i_2+nums[i])
            # 向前推一天
            dp_i_2 = dp_i_1
            dp_i_1 = re
        return re

if __name__ == '__main__':
    house = [1, 2, 3, 1]
    rel = Solution().rob6(house)
    print(rel)


