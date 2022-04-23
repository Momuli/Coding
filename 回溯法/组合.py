class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        def recur(start):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(start, n+1):
                cur.append(i)
                recur(i+1)
                cur.pop()
        recur(1)
        return res