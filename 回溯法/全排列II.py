class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        nums.sort()
        vis = [0] * len(nums)
        def recur(x, l):
            if x == l:
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if vis[i] == 1 or i > 0 and nums[i] == nums[i-1] and vis[i-1] == 0:
                    continue
                vis[i] = 1
                cur.append(nums[i])
                recur(x+1, l)
                cur.pop()
                vis[i] = 0
        recur(0, len(nums))
        return res

if __name__ == '__main__':
    nums = [1, 1, 2]
    rel = Solution().permuteUnique(nums)
    print(rel)