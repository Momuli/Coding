class Solution:
    def search(self , nums , target ):
        # write code here
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            # mid在左区间
            if nums[mid] > nums[0]:
                # target在左有序区间
                if nums[0] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid在右区间
            else:
                # target在右有序区间
                if nums[mid] <= target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == '__main__':
    nums = [6, 8, 10, 0, 2, 4]
    target = 10
    rel = Solution().search(nums, target)
    print(rel)


