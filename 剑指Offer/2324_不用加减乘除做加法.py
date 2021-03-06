class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a = a & x    # 只保留数字的前32位
        b = b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x    # sum = 非进位 + 进位
        if a <= 0x7fffffff:   # 正数
            return a
        else:
            return ~(a ^ x)

if __name__ == '__main__':
    a = 1
    b = 2
    rel = Solution().add(a, b)
    print(rel)