class Solution(object):
    def isSubsequence1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = False
        if len(s) == 0:
            flag = True
        i = 0
        j = 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
        if i == len(s):
            flag = True
        return flag

    def isSubsequence2(self, s, t):
        len_s = len(s)
        len_t = len(t)
        dp = [[0] * 26 for _ in range(len(t))]
        dp.append([len_t]*26)
        # 填dp表：d[i][j]:从t[i]开始第j(a-z)个元素首次出现的下标
        # dp表的行：t中的每个字符
        # dp表的列：26个字母(a-z)
        for i in range(len_t-1, -1, -1):
            for j in range(26):
                if ord(t[i]) == j + ord('a'):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]
        m = 0   # 控制行
        for k in range(len_s):
            if dp[m][ord(s[k])-ord('a')] == len_t:
                return False
            m = dp[m][ord(s[k])-ord('a')] + 1
        return True




if __name__ == '__main__':
    s = "ahc"
    t = "ahbgdc"
    rel = Solution().isSubsequence2(s, t)
    print(rel)
