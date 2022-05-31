# 寻找以heights[i]为高度的矩形的最大面积:向左向右两个方向寻找严格比heights[i]小的元素，作为矩形的左右边界
# 维护一个单调栈：栈中元素严格单调递增
# 如果当前元素比栈顶元素大，证明找到了以栈顶元素为高的矩形的右边界
# 栈中存储高度的索引
class Solution:
    def largestRectangleArea(self, heights):
        res = 0    # 存储最大值
        heights.append(-1)    # 避免栈中最小元素无法弹出找
        stack = []   # 单调递增栈
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                # 找到了stack[-1]的右边界
                cur = stack.pop()
                # 如果不为空
                if stack:
                    # 因为栈是严格递增的，所以左边界就是弹出cur之后的栈顶元素
                    cur_s = (i - stack[-1] - 1) * heights[cur]
                else:
                    # 栈为空，相当于弹出了栈中的最后一个元素，它的左边界就是-1
                    cur_s = (i - (-1) -1) * heights[cur]
                res = max((res, cur_s))
            stack.append(i)
        return res

num = [2,1,5,6,2,3]
rel = Solution().largestRectangleArea(num)
print(rel)