class Solution:
    # 双指针
    def maxArea(self, height ):
        # write code here
        if len(height) <= 1:
            return 0
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            res = max(res, min(height[left], height[right])*(right-left))
            # 盛水多少取决于短板,因此哪边的值小就改变哪边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res