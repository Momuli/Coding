class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums):
            cur_num = nums[i]
            three_res = self.threeSum(nums, target-cur_num, i+1)
            if three_res:
                for item in three_res:
                    item.append(cur_num)
                    res.append(item)
            while i < len(nums) and nums[i] == cur_num:
                i += 1
        return res
    def threeSum(self, nums, target, start):
        res = []
        i = start
        while i < len(nums):
            cur_num = nums[i]
            two_res = self.twoSum(nums, target-cur_num, i+1)
            if two_res:
                for item in two_res:
                    item.append(cur_num)
                    res.append(item)
            while i < len(nums) and nums[i] == cur_num:
                i += 1
        return res
    def twoSum(self, nums, target, start):
        left = start
        right = len(nums)-1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            cur_left = nums[left]
            cur_right = nums[right]
            if sum > target:
                while left < right and nums[right] == cur_right:
                    right -= 1
            elif sum < target:
                while left < right and nums[left] == cur_left:
                    left += 1
            else:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == cur_left:
                    left += 1
                while left < right and nums[right] == cur_right:
                    right -= 1
        return res

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    target = 8
    rel = Solution().fourSum(nums, target)
    print(rel)