class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        l = self.left_bound(nums, target)
        r = self.right_bound(nums, target)
        res.extend([l])
        res.extend([r])
        return res

    def left_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:  # 寻找左边界
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        else:
            return left
    def right_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right= mid - 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        else:
            return right
if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    nums = []
    target = 0
    rel = Solution().searchRange(nums,target)
    print(rel)