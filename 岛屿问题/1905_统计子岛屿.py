class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        res = 0  # 用于记录子岛屿总数
        height = len(grid1)
        width = len(grid1[0])
        # 遍历二维数组中的每一个元素
        for i in range(height):
            for j in range(width):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    self.fill_0(grid2, i, j)

        for i in range(height):
            for j in range(width):
                if grid2[i][j] == 1:
                    self.fill_0(grid2, i, j)
                    res += 1
        return res

    # 将陆地(1)用海水(0)淹没      # 如果能形成岛屿,那么陆地的数目大于等于1,并且是相邻的
    def fill_0(self, grid, row, col):
        # base case
        # 1.索引超出边界
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
            return
        # 2.grid2[col][row]已经 == '0'
        if grid[row][col] == 0:
            return

        grid[row][col] = 0
        self.fill_0(grid, row - 1, col)   # 上方
        self.fill_0(grid, row + 1, col)   # 下方
        self.fill_0(grid, row, col - 1)   # 左方
        self.fill_0(grid, row, col + 1)   # 右方

if __name__ == '__main__':
    grid1 = [[1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 1, 0]]
    grid3 = [[1, 0, 1, 0, 1],
             [1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [1, 0, 1, 0, 1]]
    grid4 = [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1]]

    rel = Solution().countSubIslands(grid1, grid2)
    print(rel)