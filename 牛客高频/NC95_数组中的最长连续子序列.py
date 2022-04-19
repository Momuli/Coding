class Solution:
    # 滑动窗口法
    def MLS(self , arr):
        # write code here
        arr = list(set(arr)) # 数组中元素去重
        arr.sort()
        res = 0
        left = 0
        right = 0
        while right < len(arr):
            if right - left + 1 == arr[right] - arr[left] + 1:
                res = max(right-left+1, res)
                right += 1
            else:
                left += 1
        return res
