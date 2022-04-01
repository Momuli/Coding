class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            # 以s[i]为中心向两边扩散
            s1 = self.subrome(s, i, i)
            s2 = self.subrome(s, i, i+1)
            if len(res) < len(s1):
                res = s1
            if len(res) < len(s2):
                res = s2
        return res

    def subrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

if __name__ == '__main__':
    s = "abbba"
    rel = Solution().longestPalindrome(s)
    print(rel)