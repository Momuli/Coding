class Solution(object):
    # 最小代价
    def minDistance(self, word1, word2, ic, dc, rc):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s1 = len(word1)
        s2 = len(word2)
        # dp[i][j]:word1[:i]和word[:j]匹配需要的最小代价
        dp = [[0 for _ in range(s2+1)] for _ in range(s1+1)]
        # word1 -> ''：只能删除
        for i in range(1, s1+1):
            dp[i][0] = dp[i-1][0] + dc
        # '' -> word2:只能插入
        for j in range(1, s2+1):
            dp[0][j] = dp[0][j-1] + ic
        for i in range(1, s1+1):
            for j in range(1, s2+1):
                # word[i-1]和word[j-1]相等:不需要任何操作,因此等于word1[:i-1]和word[:j-1]匹配需要的最小代价
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                # word[i-1]和word[j-1]相等:需要从删除,插入和替换中选择一种最小代价
                    dp[i][j] = min(dp[i-1][j-1]+rc, dp[i-1][j]+dc, dp[i][j-1]+ic)
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "abc"
    s2 = "adc"
    ic = 5
    dc = 3
    rc = 100
    rel = Solution().minDistance(s1, s2, ic, dc, rc)
    print(rel)