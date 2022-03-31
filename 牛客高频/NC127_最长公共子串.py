class Solution:
    def LCS1(self, str1, str2):
        # write code here
        left = 0
        res = ''
        for i in range(len(str1)+1):
            if str1[left:i+1] in str2:
                res = str1[left:i+1]
            else:
                left += 1
        return res
# 最长公共子串的长度
    def LCS2(self, str1, str2):
        len_1 = len(str1)
        len_2 = len(str2)
        dp = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
        res = 0
        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res

if __name__ == '__main__':
    str1 = "1AB2345CD"
    str2 = "12345EF"
    rel = Solution().LCS2(str1, str2)
    print(rel)


