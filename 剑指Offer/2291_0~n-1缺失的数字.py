class Solution(object):
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
            else:
                return i
        return i
    # 二分查找
    def missingNumber2(self, nums):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            # mid位于左子区间:nums[i]==i,右子区间首元素位于[mid+1,right]之间
            if nums[mid] == mid:
                left = mid + 1
            # mid位于右子区间,左子区间的末元素位于[left,mid-1]之间
            elif nums[mid] != mid:
                right = mid - 1
        return left


if __name__ == '__main__':
    nums = [0]
    rel = Solution().missingNumber2(nums)
    print(rel)