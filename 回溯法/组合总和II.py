class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        cur = []
        def recur(start, summ):
            if summ == target:
                res.append(cur[:])
                return
            if summ > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                summ += candidates[i]
                # 每个元素只能使用一次,不能重复使用
                recur(i+1, summ)
                cur.pop()
                summ -= candidates[i]
        recur(0, 0)
        return res
