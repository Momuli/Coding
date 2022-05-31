# 定义当前可以到达的最远位置max_idx
# 如果能到达位置i,那么它前面的位置都可以到达
# 根据i+num[i]更新当前能到达的最远位置
class Solution:
    def canJump(self, nums):
        max_idx = 0
        for i in range(len(nums)):
            # 如果当前位置i<=max_idx,那么当前位置i一定是可以到达的
            if i <= max_idx and i + nums[i] > max_idx:
                max_idx = i + nums[i]
        return max_idx >= len(nums) - 1
