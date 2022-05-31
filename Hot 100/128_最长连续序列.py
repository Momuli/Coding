# 去重之后排序+滑动窗口判断
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        left = 0
        right = 0
        res = 0
        while right < len(nums):
            if nums[right] - nums[left] == right - left:
                res = max(res, right-left+1)
                right += 1
            else:
                left = right
                right += 1
        return res

nums = [0, 1, 1 ,2]
rel = Solution().longestConsecutive(nums)
print(rel)