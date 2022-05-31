# 从上到下:&运算确定最大高度
# 从左往右:&+>>运算确定最大宽度
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return
        # 将每一行变成二进制的数字
        # [20, 23, 31, 18]
        nums = [int(''.join(row), 2) for row in matrix]
        # ans:最大面积
        # N:行数
        res, N = 0, len(nums)
        # 遍历每一行，找以第i行为起点，可以延伸的最大高度(竖直方向都为1的地方，高度+1)
        for i in range(N):
            cur = i   # 从当前行i开始向下延伸
            cur_num = nums[i]
            while cur < N:
                # num中为1的位置，说明上下两行该位置都是1，相当于求矩阵的高,高度为j - i + 1
                cur_num = cur_num & nums[cur]
                # 没有1,说明没有直达i-j行的竖直矩形
                if not cur_num:
                    break
                width = 0
                width_num = cur_num
                # 已经确定了目前达到的最大高度,确定可以达到的最大宽度,也就是相邻1的个数
                while width_num:
                    width += 1
                    width_num = width_num & (width_num >> 1)
                # 更新最大值
                res = max(res, width*(cur-i+1))
                cur += 1
        return res

matrix = [["1","0","1","0","0"],
       ["1","0","1","1","1"],
       ["1","1","1","1","1"],
       ["1","0","0","1","0"]]
rel = Solution().maximalRectangle(matrix)
print(rel)