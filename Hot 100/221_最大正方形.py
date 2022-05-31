# 以当前位置为正方形的右下角
# 考虑当前位置的左边，上边以及左上角位置对应的正方形构造情况
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 以当前位置为正方形右下角的正方形的最大边长
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # 初始化第一列
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        # 初始化第一列
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        # 转换转移
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0
        max_len = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len * max_len
