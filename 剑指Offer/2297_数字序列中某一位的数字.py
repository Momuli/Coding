class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1   # 其实数字1, 10, 100,...
        digit = 1   # 数位：1-9:1, 10-99:2, 100-999:3
        count = 9   # digit数位的总位数:count=start*9*digit
        while n > count:
            n -= count   # 找到第n位所在的count区间
            start = start * 10   # 下一个start
            digit += 1 # 下一组数的数位
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 第n位字符所在的数字
        return int(str(num)[(n-1) % digit])

if __name__ == '__main__':
    n = 11
    rel = Solution().findNthDigit(n)
    print(rel)