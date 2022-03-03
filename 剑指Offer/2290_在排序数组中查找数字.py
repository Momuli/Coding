class Solution(object):
    # 遍历
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for item in nums:
            if item == target:
                count += 1
        return count
    # 二分查找
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_idx = self.left_bound(nums, target)
        right_idx = self.right_bound(nums, target)
        if left_idx == -1 and right_idx == -1:
            return 0
        else:
            return right_idx - left_idx + 1

    def left_bound(self, nums, target):
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = right - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left += 1
        if right < 0 or nums[right] != target:
            return -1
        return right

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    rel = Solution().search2(nums, target)
    print(rel)