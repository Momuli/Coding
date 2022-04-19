class Solution:
    def permuteUnique(self , num):
        if not num or len(num) == 1:
            return [num]
        res = []
        cur = []
        vis = [0] * len(num)
        num = sorted(num)
        def recur(x, l):
            if x == l:
                res.append(list(cur))
                return
            for i in range(len(num)):
                if vis[i] == 1 or  i > 0 and num[i] == num[i-1] and vis[i-1] == 0:
                    continue
                cur.append(num[i])
                vis[i] = 1
                recur(x+1, l)
                cur.pop()
                vis[i] = 0
        recur(0, len(num))
        return res

if __name__ == '__main__':
    num = [1, 1, 2]
    rel = Solution().permuteUnique(num)
    print(rel)
