class Solution(object):
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = bin(int(a, 2)+int(b, 2))[2:]
        return sum

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = ""   # 保存结果
        carry = 0   # 保存进位
        # 使两个二进制字符串对齐
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b = '0' + b
        else:
            for i in range(len(b)-len(a)):
                a = '0' + a
        for i in range(len(a)-1, -1, -1):
            sum = str((int(a[i])+int(b[i])+carry) % 2) + sum
            carry = (int(a[i])+int(b[i])+carry) // 2
        if carry:
            sum = str(carry) + sum
        return sum

if __name__ == '__main__':
    a = '11'
    b = '11'
    rel = Solution().addBinary2(a, b)
    print(rel)