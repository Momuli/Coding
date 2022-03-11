class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return False
        # 去掉字符串收尾空格
        s = s.strip()
        numFlag = False
        dotFlag = False
        eFlag = False
        # 遍历s中的每一个字符
        for i in range(len(s)):
            if s[i] == ' ':
                return False
            # 当前字符为数字
            elif s[i] >= '0' and s[i] <= '9':
                numFlag = True
            # 当前字符为'.':'.'只能出现一次，并且小数只能出现在'e'之前
            elif s[i] == '.':
                if dotFlag or eFlag:
                    return False
                else:
                    dotFlag = True
            # 当前字符为'e':需要没有出现过'e',并且'e'前面要有数字
            elif s[i] == 'e' or s[i] == 'E':
                if eFlag or not numFlag:
                    return False
                else:
                    eFlag = True
                    numFlag = False   # 重置为False:当出现e后,如果e后边没有数字也是错误的
            elif s[i] == '+' or s[i] == '-':
                if s[i-1] != 'e' and s[i-1] != 'E' and i > 0:
                    return False
            else:
                return False
        return numFlag


if __name__ == '__main__':
    s = "-1E-16"
    rel = Solution().isNumber(s)
    print(rel)