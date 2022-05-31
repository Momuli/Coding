class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        left = 0
        right = 1
        while left < len(nums) and right < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
            else:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right == len(nums):
                    return
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right = left
