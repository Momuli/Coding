class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        def recur(start):
            if sum(cur) == target:
                res.append(cur[:])
                return
            if sum(cur) > target:
                return
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                # 当前元素candidates[i]可以重复使用
                recur(i)
                cur.pop()
        recur(0)
        return res