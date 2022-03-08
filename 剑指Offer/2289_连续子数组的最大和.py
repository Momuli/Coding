class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义dp数组
        dp = [nums[0]]    # dp[i]表示以nums[i]结尾的子数组的最大和
        for i in range(1, len(nums)):
        # 当nums[i]之前的元素的和<0时,直接丢弃,只会对nums[i]产生负贡献
            if dp[i-1] <= 0:
                dp.append(nums[i])
        # 当nums[i]之前的元素和>0时,保留
            else:
                dp.append(nums[i]+dp[i-1])
        return max(dp)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    rel = Solution().maxSubArray(nums)
    print(rel)