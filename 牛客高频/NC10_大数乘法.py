class Solution:
    def solve(self, s, t):
        if s == '0' or t == '0':
            return '0'
        # 11*99:可以拆解为从末尾开始 1*99 + 10 * 99    123*99 = 3*99+20*99+100*99
        dig = 0
        res = 0
        i = len(s) - 1
        while i >= 0:
            temp = int(s[i]) * (10 ** dig) * int(t)
            res += temp
            dig += 1
            i -= 1
        return str(res)

if __name__ == '__main__':
    s = '0'
    t = '99'
    rel = Solution().solve(s, t)
    print(rel)