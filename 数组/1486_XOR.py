class Solution(object):
    def xorOperation(self, n, start):
        l = []
        r = 0
        for i in range(n):
            l.append(start+2*i)
            r ^= l[i]
        return r

n = 10
start = 5
r = Solution().xorOperation(n, start)
print(r)
