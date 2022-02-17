class Solution(object):
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set = []
        for i in range(len(nums)):
            if nums[i] not in set:
                set.append([nums[i]])
            else:
                return True
        return False

    def containsDuplicate2(self, nums):
        ori_len = len(nums)
        no_len = len(set(nums))
        if ori_len != no_len:
            return True
        return False

if __name__ == '__main__':
    num = [1,4]
    rel = Solution().containsDuplicate2(num)
    print(rel)