from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)   # 记录s中每个字符出现的次数
        res = 0
        for item in counter.values():
            res += item // 2 * 2
            if res % 2 == 0 and item % 2 == 1:
                res += 1
        return res

if __name__ == '__main__':
    s = "abccccdd"
    rel = Solution().longestPalindrome(s)
    print(rel)
