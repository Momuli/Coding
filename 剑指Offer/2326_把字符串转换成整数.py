class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        cur = 1   # 当前需要转换的字符的索引
        sign = 1   # 存储数字的符号(+,-)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        bound = INT_MAX // 10   # 判断数字是否越界
        res = 0
        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            cur = 0
        for item in str[cur:]:
            # 非数字字符
            if not '0' <= item <= '9':
                break
            # 越界
            if res == bound and item > '7' or res > bound:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            res = res * 10 + int(item)
        return res * sign

if __name__ == '__main__':
    s = '    - '
    rel = Solution().strToInt(s)
    print(rel)