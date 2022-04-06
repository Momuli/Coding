class Solution:
    def maxWater(self , arr):
        if len(arr) <= 2:
            return 0
        water = 0
        max_value = 0
        max_idx = 0
        # 找最大值及最大索引
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
                max_idx = i
        # 左边
        left = arr[0]
        for right in arr[1:max_idx+1]:
            if right < left:
                water += left - right
            else:
                left = right
        # 右边
        right = arr[-1]
        for left in arr[len(arr)-2:max_idx-1:-1]:
            if left < right:
                water += right - left
            else:
                right = left
        return water

if __name__ == '__main__':
    ss = [4,5,1,3,2]
    rel = Solution().maxWater(ss)
    print(rel)
