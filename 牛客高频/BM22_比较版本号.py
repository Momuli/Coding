class Solution:
    # 遍历比较
    def compare1(self , version1: str, version2: str) -> int:
        # write code here
        # 字符串分割为列表
        s1 = version1.split('.')
        s2 = version2.split('.')
        max_len = max(len(s1), len(s2))
        for i in range(max_len):
            # 超出列表长度补0
            if i > len(s1) - 1:
                s1.append('0')
            if i > len(s2) - 1:
                s2.append('0')
            # 元素以0开头
            if len(s1[i]) > 1 and s1[i][0] == '0':
                s1[i] = s1[i][1:]
            if len(s2[i]) > 1 and s2[i][0] == '0':
                s2[i] = s2[i][1:]
            if int(s1[i]) > int(s2[i]):
                return 1
            if int(s1[i]) < int(s2[i]):
                return -1
            else:
                continue
        return 0
    # 双指针
    def compare2(self , version1: str, version2: str) -> int:
        # 定义双指针分别指向version1, version2首位
        p1 = 0
        p2 = 0
        while p1 < len(version1) or p2 < len(version2):
            # 每个分割'.'前的元素大小
            num1 = 0
            num2 = 0
            while p1 < len(version1) and version1[p1] != '.':
                num1 = num1 * 10 + int(version1[p1])
                p1 += 1
            while p2 < len(version2) and version2[p2] != '.':
                num2 = num2 * 10 + int(version2[p2])
                p2 += 1
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            else:
                p1 += 1
                p2 += 1
        return 0

if __name__ == '__main__':
    s1 = "1.1.01"
    s2 = "1.01"
    rel = Solution().compare2(s1, s2)
    print(rel)