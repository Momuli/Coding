class Solution(object):
    def printNumbers1(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10**n):
            res.append(i)
        return res

    # 递归,考虑大数问题
    def printNumbers2(self, n):
        self.cur = ''
        self.res = []   # 用于存储所有生成的数字

        for i in range(1, n+1):
            self.dfs(0, i)
        return self.res

    # 需要确定的数字的长度为l,正在确定第x位
    def dfs(self, x, l):
        # x从0开始,当x==len时,表示当前数字的所有位已经生成完毕
        if x == l:
            self.res.append(int(self.cur))
            return
        else:
            # 当x=0时:表示目前需要生成左边第一位数字,最高位数字不能为0
            start = 1 if x == 0 else 0
            for i in range(start, 10):
                self.cur += str(i)   # 确定第x位数字
                self.dfs(x+1, l)   # 递归处理第x+1位
                self.cur = self.cur[:len(self.cur)-1]   # 撤销选择

if __name__ == '__main__':
    n = 2
    rel = Solution().printNumbers2(n)
    print(rel)
