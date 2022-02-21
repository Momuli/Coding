class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0  # 记录封闭岛屿的总面积
        height = len(grid)
        width = len(grid[0])
        # 淹没上边界和下边界的陆地(不是封闭岛屿)
        for i in range(width):
            self.fill_0(grid, 0, i)
            self.fill_0(grid, height-1, i)
        # 淹没左边界和右边界的陆地
        for j in range(height):
            self.fill_0(grid, j, 0)
            self.fill_0(grid, j, width-1)
        # 遍历数组中的每一个节点
        res = 0
        for i in range(1, height-1):
            for j in range(1, width-1):
                if grid[i][j] == 1:
                    res += 1
        return res
    # 将陆地(1)用海水淹没(0)
    def fill_0(self, grid, row, col):
        # 索引超出边界
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return

        # 已经是海水(0)了
        if grid[row][col] == 0:
            return

        # 否则,将当前节点淹没为海水(0),并递归处理其邻接的四个节点
        grid[row][col] = 0
        self.fill_0(grid, row-1, col)  # 上方
        self.fill_0(grid, row+1, col)  # 下方
        self.fill_0(grid, row, col-1)  # 左方
        self.fill_0(grid, row, col+1)  # 右方

if __name__ == '__main__':
    grid1 = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    grid2 = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    rel = Solution().numEnclaves(grid1)
    print(rel)