class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res = max(self.max_pro2(nums, 0, len(nums)-2), self.max_pro2(nums, 1, len(nums)-1))
        return res
    # 计算nums[start]-nums[end]被抢时,获得的最大利润
    def max_pro1(self, nums, start, end):
        # 定义dp数组
        # dp[i]:从第i间房子开始抢,可以获得的最高金额
        dp = [-1] * (len(nums)+2)
        # base case
        dp[-1] = 0
        dp[-2] = 0
        if end == len(nums) - 2:
            dp[-3] = 0
        for i in range(end, start-1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        return dp[start]
    # 空间优化
    def max_pro2(self, nums, start, end):
        dp_i_1 = 0
        dp_i_2 = 0
        dp_i = 0
        for i in range(end, start-1, -1):
            dp_i = max(dp_i_1, dp_i_2+nums[i])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i

if __name__ == '__main__':
    nums = [2, 3, 2]
    rel = Solution().rob(nums)
    print(rel)