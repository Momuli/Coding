class Solution (object):
    def newways(self, n):
        if n < 2:
            return 1
        mod = 10**9+7
        p = 0
        q = 1
        r = 1
        for i in range(2, n+1):
            p = q
            q = r
            r = p + q
        return r % mod

if __name__ == '__main__':
    n = 7
    rel = Solution().newways(n)
    print(rel)

