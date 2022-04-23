class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        cur = []
        def recur(start):
            res.append(cur[:])
            for i in range(start, len(nums)):
                # 剪枝:与前一个元素相同则跳过
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                recur(i+1)
                cur.pop()
        recur(0)
        return res