class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len_1 = len(text1)
        len_2 = len(text2)
        # dp[i][j]表示text1[:i+1]与text[:j+1]的最长公共子序列
        dp = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]
        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    rel = Solution().longestCommonSubsequence(text1, text2)
    print(rel)