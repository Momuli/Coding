class Solution:
    # 上坡度,下坡度和峰值
    def candy1(self , arr):
        # write code here
        # 初始化:当只有一个元素时
        res = 1   # 糖果总数
        peak = 1  # 峰顶高度
        up = 0   # 上坡度
        down = 0  # 下坡度
        # 从第二个元素开始判断
        for i in range(1, len(arr)):
            res += 1   # 每个元素先分配一个糖果
            if arr[i] > arr[i-1]:
                up += 1   # 上坡高度差+1
                res = res + up   # 当前元素的糖果数比坡底元素多up个
                down = 0
                peak = up + 1   # 峰顶高度
            elif arr[i] == arr[i-1]:
                up = 0   # 连续上坡元素数置为0
                down = 0
                peak = 0  # 当前没有峰顶
            elif arr[i] < arr[i-1]:
                res = res + down   # down为上一轮的高度差,down具有滞后性(如果只有一个元素下降，那么它的糖果数直接为1)
                down += 1
                up = 0
                # 峰顶处的糖果数取决于下坡个数和上坡个数的最大值
                if down >= peak:
                    res += 1
        return res
    # 两遍遍历同时满足左右规则
    def candy2(self, arr):
        temp = [1] * len(arr)
        # 从左向右遍历:右边数比左边数大，糖果数加1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                temp[i] = temp[i-1] + 1
        # 从右向左遍历:左边数比右边数大并且左边的糖果<=右边的糖果
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1] and temp[i] <= temp[i+1]:
                temp[i] = temp[i+1]
        return sum(temp)
