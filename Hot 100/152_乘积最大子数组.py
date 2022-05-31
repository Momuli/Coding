# 由于存在负数，因此不能想子数组和那样只考虑当前元素大小和前一个元素的最大子数组和
# 以负数结尾的乘积可以负负得正
# 如果当前是正数，就希望之前的乘积尽可能大
# 如果当前为负数，就希望之前的乘积尽可能小
# 保存每个位置的最大乘积和最小乘积
class Solution:
    def maxProduct(self, nums):
        dp = [[0, 0] for _ in range(len(nums))]
        # 最大值
        dp[0][0] = nums[0]
        # 最小值
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        return max(dp)[0]

nums = [5, 6, -3, 4, -3]
rel = Solution().maxProduct(nums)
print(rel)
