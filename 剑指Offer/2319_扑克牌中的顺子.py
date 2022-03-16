class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)   # 数组排序
        joker = 0   # 统计0的个数
        for i in range(len(nums)-1):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[-1]-nums[joker]<5