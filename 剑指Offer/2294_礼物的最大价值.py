class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(grid)
        len_col = len(grid[0])
        for i in range(len_row):
            for j in range(len_col):
                # 第一行元素:只能从它的左侧元素到达
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                # 第一列元素:只能从它的上方元素到达
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i-1][j]
                # 其他元素可以从左侧或者上方元素到达
                elif i != 0 and j != 0:
                    grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

if __name__ == '__main__':
    nums = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    rel = Solution().maxValue(nums)
    print(rel)