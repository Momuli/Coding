class Solution(object):
    def exchange1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return nums
        left = 0
        right = len(nums)-1
        while left < right:
            # 左偶右奇:交换
            if nums[left] % 2 == 0 and nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            # 左偶右偶
            elif nums[left] % 2 == 0 and nums[right] % 2 == 0:
                cur = nums.pop(left)
                nums.append(cur)
                right -= 2
            # 左奇右奇
            elif nums[left] % 2 == 1 and nums[right] % 2 == 1:
                cur = nums.pop(right)
                nums.insert(0, cur)
                left += 2
            # 左奇右偶
            elif nums[left] % 2 == 1 and nums[right] % 2 == 0:
                left += 1
                right -= 1
        return nums

    def exchange2(self, nums):
        if len(nums) == 1 or not nums:
            return nums
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    rel = Solution().exchange2(nums)
    print(rel)