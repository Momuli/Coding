class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        left = 1
        right = 2
        while left < right:
            summ = (right + left) * (right - left + 1) / 2
            if summ > target:
                left += 1
            elif summ < target:
                right += 1
            else:
                cur = []
                for i in range(left, right+1):
                    cur.append(i)
                res.append(cur)
                right += 1
                left += 1
        return res

if __name__ == '__main__':
    target = 9
    rel = Solution().findContinuousSequence(target)
    print(rel)