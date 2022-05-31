# 逆序遍历+维护降序单调栈
class Solution:
    def dailyTemperatures(self, temperatures):
        que = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while que and temperatures[que[-1]] <= temperatures[i]:
                que.pop()
            if que:
                res[i] = que[-1] - i
            else:
                res[i] = 0
            que.append(i)
        return res