# 当遇到'['时，就将它前面已经形成的(字符串,数组)压入栈
# 遇到']'时,弹出栈顶的元祖,给已经形成的字符串后面添加子字符串
class Solution:
    def decodeString(self, s):
        res = ''
        num = 0
        stack = []
        for item in s:
            if item.isdigit():
                num = num * 10 + int(item)
            elif item == '[':
                stack.append((res, num))
                res = ''
                num = 0
            elif item == ']':
                pop_item = stack.pop()
                res = pop_item[0] + res * pop_item[1]
            else:
                res += item
        return res

s = "3[a2[c]]"
rel = Solution().decodeString(s)
print(rel)