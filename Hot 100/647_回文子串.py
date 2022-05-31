# 双指针+中心扩散法
class Solution:
    def countSubstrings(self, s):
        res = 0
        def recur(i, j):
            cur = 0
            # 记录每一个子串
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cur += 1
            return cur
        for i in range(len(s)):
            res += recur(i, i)
            res += recur(i, i+1)
        return res

s = 'aaaaa'
rel = Solution().countSubstrings(s)
print(rel)