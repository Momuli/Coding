class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.res = []
        if not nums:
            return nums
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                self.res.extend([nums[left], nums[right]])
                return self.res
        return self.res
