class Solition(object):
    def numDistinctIslands(self, grid):
        self.route_s = []
        self.route = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.fill_0(grid, i, j, 0)
                    self.route_s.append(str(self.route))
                    self.route = []
        return len(set(self.route_s))
    # 上下左右：1,2,3,4
    def fill_0(self, grid, row, col, dir):
        if row<0 or col<0 or row>=len(grid) or col>= len(grid[0]):
            return
        if grid[row][col] == 0:
            return

        # 前序位置,刚进入节点
        grid[row][col] = 0
        self.route.append(dir)
        self.fill_0(grid, row-1, col, 1)
        self.fill_0(grid, row+1, col, 2)
        self.fill_0(grid, row, col-1, 3)
        self.fill_0(grid, row, col+1, 4)

        # 后序位置,逆向回传
        self.route.append(-dir)

if __name__ == '__main__':
    grid1 = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    grid2 = [[1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1]]
    rel = Solition().numDistinctIslands(grid1)
    print(rel)