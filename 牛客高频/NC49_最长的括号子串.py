class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # 记录左括号的索引
        dp = [0] * (len(s)+1)  # dp[i]:以s[i-1]结尾的最长括号子串的长度
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                dp[i+1] = 0   # 以s[i]左括号结尾的括号子串一定是无效的
            else:
                if stack:
                    left_idx = stack.pop()   # 弹出与当前右括号匹配的左括号索引
                    # 以s[i]右括号结尾的最长括号子串的长度=当前右括号与其匹配的左括号之间的长度
                    # + 匹配的左括号之前的括号子串的长度dp[left_idx](以s[left_idx-1]结尾)
                    len_l = i - left_idx + 1 + dp[left_idx]
                    dp[i+1] = len_l
                else:
                    dp[i+1] = 0
        res = 0
        for item in dp:
            res = max(item, res)
        return res

if __name__ == '__main__':
    s =  "(())()"
    rel = Solution().longestValidParentheses(s)
    print(rel)