class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        vis = [0] * len(nums)
        def recur(x, l):
            if x == l:
                res.append(cur[:])
            for i in range(len(nums)):
                if vis[i] == 1:
                    continue
                vis[i] = 1
                cur.append(nums[i])
                recur(x+1, l)
                vis[i] = 0
                cur.pop()
        recur(0, len(nums))
        return res