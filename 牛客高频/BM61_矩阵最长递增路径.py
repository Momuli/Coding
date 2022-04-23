class Solution:
    def solve(self , matrix):
        # write code here
        if not matrix:
            return 0
        res = 0   # res保存最长距离
        # 备忘录
        memo = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # 以matrix[row][col]为起点的最长距离
        def recur(row, col, pre):
            if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0:
                return 0
            if memo[row][col] != -1:
                return memo[row][col]
            # 比前一个数小
            if pre >= matrix[row][col]:
                return 0
            cur = 0
            prev = matrix[row][col]
            # 上下左右四个方向
            cur = max(cur, recur(row-1, col, prev))
            cur = max(cur, recur(row+1, col, prev))
            cur = max(cur, recur(row, col+1, prev))
            cur = max(cur, recur(row, col-1, prev))
            # 更新备忘录
            memo[row][col] = cur + 1
            return cur + 1

        # 以矩阵中的每个点为起点计算一次最长距离
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, recur(i, j, -1))
        return res

num = [[1,2,3],[4,5,6],[7,8,9]]
num2 = [[1,2],[4,3]]
rel = Solution().solve(num2)
print(rel)