## def solve(self, s, t):
### 字符串模拟！

**思路:**
1. 将字符串`s,t`填充为相同长度
2. 逆序遍历字符串`s,t`的对应位
3. 对应位`s[i]`与`t[i]`相加
4. 如果有进位,`carry=1`

**代码:**
```
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
```