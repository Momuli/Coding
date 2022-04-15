class Solution:
    # 行:从下往上遍历, 列从左往右遍历
    def rotateMatrix(self , mat, n):
        res = []
        col = 0
        while col < n:
            cur = []
            for i in range(n-1, -1, -1):
                cur.append(mat[i][col])
            res.append(cur)
            col += 1
        return res
