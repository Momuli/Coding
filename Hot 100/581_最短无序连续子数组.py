# 原始数组排序
# 双指针对照找到左右边界
class Solution:
    def findUnsortedSubarray(self, nums):
        temp = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right and temp[left] == nums[left]:
            left += 1
        while left <= right and temp[right] == nums[right]:
            right -= 1
        return right - left + 1

nums = [2,6,4,8,10,9,15]
rel = Solution().findUnsortedSubarray(nums)
print(rel)