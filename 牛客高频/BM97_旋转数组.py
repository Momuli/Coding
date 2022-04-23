class Solution:
    def solve1(self , n , m , a ):
        # write code here
        # 计算旋转位置
        temp = m % n
        a[:temp], a[temp:] = a[-temp:], a[:n-temp]
        return a

    def solve2(self, n, m, a):
        # 先将整个数组反转,在根据移动位置分别反转两个子数组
        temp = m % n
        # 反转整个数组
        a = self.recur(a, 0, n-1)
        # 反转前半部分
        a = self.recur(a, 0, temp-1)
        # 反转后半部分
        a = self.recur(a, temp, n-1)
        return a
    # start:反转开始位置  end:反转结束位置
    def recur(self, num, start, end):
        while start < end:
            num[start], num[end] = num[end], num[start]
            start += 1
            end -= 1
        return num