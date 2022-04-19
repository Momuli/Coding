class Solution:
    def combinationSum2(self , num, target):
        res = []
        cur = []
        num = sorted(num)  # 数组排序
        def recur(start, diff):
            if diff == 0:
                res.append(cur[:])
                return
            for i in range(start, len(num)):
                if i > start and num[i] == num[i-1]:
                    continue
                if num[i] <= diff:
                    cur.append(num[i])
                    recur(i+1, diff-num[i])
                    cur.pop()
        recur(0, target)
        return res

if __name__ == '__main__':
    num =  [100,10,20,70,60,10,50]
    target = 80
    rel = Solution().combinationSum2(num, target)
    print(rel)