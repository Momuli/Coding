class Solution:
    def removeInvalidParentheses(self, s):
        def isvalid(string):  # 判断括号串是否合法
            count = 0
            for c in string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        # level:初始化第一层的字符串
        level = {s}
        while True:  # BFS
            # 从当前层中挑选出合法的字符串
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            # 新的层中的字符串
            new_level = set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in '()':
                        # 每次删除当前字符s[i]构成新的字符串
                        new_level.add(s[:i]+s[i+1:])
            # 检查新生成的一层字符串是否包含合法字符串
            level = new_level

s = "()())()"
rel = Solution().removeInvalidParentheses(s)
print(rel)