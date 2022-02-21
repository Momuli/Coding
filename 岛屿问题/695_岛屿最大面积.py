class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.res = 0  # 用于记录岛屿最大面积
        self.cur = 0  # 记录当前岛屿面积
        # 遍历二维数组中的每一个元素
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:    # 岛屿数+1
                    self.fill_0(grid, i, j)
                    self.res = max(self.res, self.cur)
                    self.cur = 0
        return self.res

    # 将陆地(1)用海水(0)淹没      # 如果能形成岛屿,那么陆地的数目大于等于1,并且是相邻的
    def fill_0(self, grid, row, col):
        # base case
        # 1.索引超出边界
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
            return

        # 2.grid[col][row]已经 == '0'
        if grid[row][col] == 0:
            return

        grid[row][col] = 0
        self.cur += 1
        self.fill_0(grid, row-1, col)  # 上方
        self.fill_0(grid, row+1, col)  # 下方
        self.fill_0(grid, row, col-1)  # 左方
        self.fill_0(grid, row, col+1)  # 右方

if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    rel = Solution().maxAreaOfIsland(grid)
    print(rel)