class Solution(object):
    def findRepeatNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for item in nums:
            if item not in num_set:
                num_set.add(item)
            else:
                return item
        return -1

    def findRepeatNumber2(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    rel = Solution().findRepeatNumber2(l)
    print(rel)