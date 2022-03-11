class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        self.res = []
        # 定义上下左右四个边界
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        while True:
            for i in range(l, r+1):
                self.res.append(matrix[t][i])   # 从左往右
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                self.res.append(matrix[i][r])   # 从上到下
            r -= 1
            if r < l:
                break
            for i in range(r, l-1, -1):
                self.res.append(matrix[b][i])  # 从右向左
            b -= 1
            if b < t:
                break
            for i in range(b, t-1, -1):
                self.res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return self.res

if __name__ == '__main__':
    nums1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    nums2 = [[3], [2]]
    rel = Solution().spiralOrder(nums1)
    print(rel)