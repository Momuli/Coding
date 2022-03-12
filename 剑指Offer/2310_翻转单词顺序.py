class Solution(object):
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()   # 删除字符串的收尾空格
        l_s = s.split()  # 将字符串拆分为数组
        l_s.reverse()
        return ' '.join(l_s)

    def reverseWords2(self, s):
        s = s.strip()
        left = right = len(s) - 1
        res = []
        while left >= 0:
            while left >= 0 and s[left] != ' ':
                left -= 1
            res.append(s[left+1:right+1])
            while left >= 0 and s[left] == ' ':
                left -= 1
            right = left
        return ' '.join(res)

if __name__ == '__main__':
    s = "a good   example"
    rel = Solution().reverseWords2(s)
    print(rel)