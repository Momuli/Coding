class Solution:
    # 先求最长公共子序列的长度，然后从右下角向前回溯找最长公共子序列
    def LCS(self , s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        res = ''
        m, n = len1, len2
        while m >= 1 and n >= 1:
            if s1[m-1] == s2[n-1]:
                res += s1[m-1]
                n -= 1
                m -= 1
            elif dp[m-1][n] > dp[m][n-1]:
                m -= 1
            else:
                n -= 1
        if not res:
            return -1
        else:
            return res[::-1]

if __name__ == '__main__':
    s1 = "1A2C3D4B56"
    s2 = "B1D23A456A"
    rel = Solution().LCS(s1, s2)
    print(rel)