# nums中的值为1-n
# 将以nums中的值val为下标的对应的值改为负值
# 遍历数组,数组中不是负值的数对应的索引idx+1就为缺失的值
class Solution:
    def findDisappearedNumbers(self, nums):
        for item in nums:
            nums[abs(item)-1] = -abs(nums[abs(item)-1])
        res = []
        for idx, val in enumerate(nums):
            if val > 0:
                res.append(idx+1)
        return res

nums = [1, 3, 5, 3, 4, 4]
rel = Solution().findDisappearedNumbers(nums)
print(rel)