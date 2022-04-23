class Solution:
    def Nqueen(self , n ):
        # write code here
        self.res = 0
        col = [] # 列
        zheng = []  # 正斜线方向    # 如果在同一条斜线上,那么row-col or row + col相等
        fan = []  # 反斜线方向

        # 给第row行放皇后
        def recur(row, n):
            if row == n:
                self.res += 1
                return
            #每一列判断
            for j in range(n):
                if j in col or row-j in zheng or row+j in fan:
                    continue
                col.append(j)
                zheng.append(row-j)
                fan.append(row+j)
                recur(row+1, j)  # 确定下一行
                col.pop()
                zheng.pop()
                fan.pop()
        recur(0, n)
        return self.res