class Solution(object):
    # 模拟法
    def lastRemaining1(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # 环
        cycle = [i for i in range(n)]
        idx = 0    # 要删除的索引
        while len(cycle) > 1:
            idx = (idx + m - 1) % n    # 计算每一次要删除元素的索引
            del cycle[idx]
            n -= 1     # 长度减一
        return cycle[0]

    # 数学
    def lastRemaining2(self, n, m):
        # 从后往前推
        idx = 0    # 最后的索引为0
        l = 1   # 最后的长度为1
        while l < n:
            l += 1
            idx = (idx + m) % l
        return idx

if __name__ == '__main__':
    n = 5
    m = 3
    rel = Solution().lastRemaining2(n, m)
    print(rel)