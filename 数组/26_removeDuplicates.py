class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums)-1):
            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                del nums[j]
            else:
                i += 1
        return len(nums), nums

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            i = 0   # 慢指针
            for j in range(1, len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
            return i+1, nums
        else:
            return 0

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    len_nums, new_nums = Solution().removeDuplicates2(nums)
    print(len_nums)
    print(new_nums)