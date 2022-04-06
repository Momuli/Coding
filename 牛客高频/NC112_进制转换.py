class Solution:
    def solve(self, M, N):
        temp = '0123456789ABCDEF'
        sign = False  # 正负数标识
        res = ''
        if M == 0:
            return '0'
        if M < 0:
            sign = True
            M = -M
        while M > 0:
            res = res + temp[M%N]
            M = M // N
        if sign:
            res = res + '-'
        return res[::-1]

if __name__ == '__main__':
    num = -10
    rel = Solution().solve(num, 16)
    print(rel)
