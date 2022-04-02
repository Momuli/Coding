class Solution:
    # 二分法
    def sqrt1(self , x ):
        # write code here
        if x <= 0:
            return 0
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
        return right
    # 牛顿法
    def sqrt2(self, x):
        if x <= 0:
            return 0
        ori = x
        while ori > x / ori:
            ori = (ori + x / ori) / 2
        return ori

if __name__ == '__main__':
    n = 9
    rel = Solution().sqrt1(n)
    print(rel)