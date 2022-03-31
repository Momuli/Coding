class Solution:
    def isValid(self, s ):
        if not s:
            return False
        stack = []
        for item in s:
            if item == '{' or item == '[' or item == '(':
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == ']' and stack.pop() != '[':
                    return False
                if item == '}' and stack.pop() != '{':
                    return False
                if item == ')' and stack.pop() != '(':
                    return False
        if not stack:
            return True
        else:
            return False

if __name__ == '__main__':
    s = '}{{(}}'
    rel = Solution().isValid(s)
    print(rel)

