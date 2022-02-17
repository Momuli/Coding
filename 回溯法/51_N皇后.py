class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []   # 存储所有结果
        track = ['.'*n] * n   # 存储当前结果
        self.Nqueen(0, track, res)  # 从第0行开始处理
        return res
    # 回溯递归函数
    # row表示第row行
    def Nqueen(self, row, track, res):
        # base case 处理
        if len(track) == row:
            res.append(list(track))
            return
        s = len(track[0])  # s表示列数
        for i in range(s):
            # 不恰当解处理
            if not self.valid(track, row, i):
                continue
            # 做选择
            track[row] = track[row][:i]+'Q'+track[row][i+1:]   # 替换字符串指定位置的元素  切片法
            # 递归处理下一行
            self.Nqueen(row+1, track, res)
            # 撤销选择
            track[row] = track[row].replace('Q', '.')

    def valid(self, track, row, col):
        # 检查列是否有冲突
        l = len(track)   # l表示行数
        for p in range(l):
            if track[p][col] == 'Q':
                return False
        # 检查左上
        i = row-1
        j = col-1
        while (i>=0 and j>=0):
            if track[i][j] == 'Q':
                return False
            else:
                i -= 1
                j -= 1
        # 检查右上
        m = row-1
        k = col+1
        while (m>=0 and k<l):
            if track[m][k] == 'Q':
                return False
            else:
                m -= 1
                k += 1
        return True

if __name__ == '__main__':
    n = 4
    rel = Solution().solveNQueens(n)
    print(rel)