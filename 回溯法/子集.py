class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []   # 存储所有子集
        cur = []   # 存储当前子集
        # 遍历回溯树的第i层
        def recur(start):
            # 前序位置
            res.append(cur[:])
            if len(cur) == len(nums):
                return
            # 选择列表
            for i in range(start, len(nums)):
                # 做选择
                cur.append(nums[i])
                # 递归遍历i+1层
                recur(i+1)
                # 撤销选择
                cur.pop()
        recur(0)
        return res
