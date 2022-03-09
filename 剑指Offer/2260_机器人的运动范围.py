class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # 递归函数
        def recur(i, j):
            # 求数位和
            def sum(n):
                s = 0
                while n:
                    s += n % 10
                    n //= 10
                return s
            # base case
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1 or sum(i)+sum(j) > k:
                return
            if sum(i) + sum(j) <= k and grid[i][j] == 0:
                self.res += 1
                # 防止重复遍历
                grid[i][j] = 1
                # 向下或者向右
                recur(i+1, j)
                recur(i, j+1)
                return

        self.res = 0
        recur(0, 0)
        return self.res

if __name__ == '__main__':
    m = 11
    n = 8
    k = 16
    rel = Solution().movingCount(m, n, k)
    print(rel)


