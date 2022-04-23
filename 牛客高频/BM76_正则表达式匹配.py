class Solution:
    # 二维dp表格
    def match(self, s, pattern ):
        len_s = len(s)
        len_p = len(pattern)
        # 二维dp表格,dp[i][j]:s[:i]与pattern[:j]是否匹配
        dp = [[False for _ in range(len_p+1)] for _ in range(len_s+1)]
        for i in range(len_s+1):
            for j in range(len_p+1):
                # 当模式串为空时: 只与空串匹配
                if j == 0:
                    dp[i][j] = i == 0
                # 当模式串不为空时:
                else:
                    # 不以'*'结尾: 'c*'看做一个整体
                    if pattern[j-1] != '*':
                        # '.'和'字母'两种情况
                        if i > 0 and j > 0 and (s[i-1] == pattern[j-1] or pattern[j-1] == '.'):
                            dp[i][j] = dp[i-1][j-1]
                    # 以'*'结尾: 'c*'看做一个整体
                    else:
                        # s[i-1]与p[j-2]('c')不匹配:'c*'作废
                        if j > 1:
                            dp[i][j] = dp[i][j-2]
                        # s[i-1]与'c'匹配
                        if j > 1 and i > 0 and (s[i-1] == pattern[j-2] or pattern[j-2] == '.'):
                            dp[i][j] |= dp[i-1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s = "aaab"
    p = "a*a*a*c"
    rel = Solution().match(s, p)
    print(rel)