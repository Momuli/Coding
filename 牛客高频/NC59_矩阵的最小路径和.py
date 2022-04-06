class Solution:
    # 动态规划:从右下角往前看
    def minPathSum(self, matrix):
        # write code here
        dp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        dp[0][0] = matrix[0][0]
        for col in range(1, len(matrix[0])):
            dp[0][col] = dp[0][col-1] + matrix[0][col]
        for row in range(1, len(matrix)):
            dp[row][0] = dp[row-1][0] + matrix[row][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        return dp[-1][-1]