class Solution:
    def solve(self, s, t):
        len_s = len(s)
        len_t = len(t)
        max_len = max(len_t, len_s)
        s = s.zfill(max_len)   # 将字符串填充为长度为max_len的串, 原字符串右对齐
        t = t.zfill(max_len)
        carry = 0   # 进位
        res = ''  # 非进位
        # 倒序遍历
        for i in range(max_len-1, -1, -1):
            temp = int(s[i]) + int(t[i]) + carry
            if temp >= 10:
                temp -= 10
                carry = 1
            else:
                carry = 0
            res = str(temp) + res
        if carry:
            res = str(1) + res
        return res

if __name__ == '__main__':
    s='10'
    t='99'
    rel = Solution().solve(s, t)
    print(rel)
