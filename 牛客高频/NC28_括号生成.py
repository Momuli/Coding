class Solution:
    def generateParenthesis(self , n):
        if n <= 0:
            return []
        res = []
        self.recur(res, '', 0, 0, n)
        return res
    def recur(self, res, cur, left, right, n):
        # 如果当前左括号的个数小于右括号的个数:不符合
        if left < right:
            return
        # 当前左括号和右括号的个数达到给定值n
        if left == n and right == n:
            res.append(cur)
        if left < n:
            self.recur(res, cur+'(', left+1, right, n)
        # 当左括号比右括号多时,可以添加右括号
        if left > right:
            self.recur(res, cur+')', left, right+1, n)
