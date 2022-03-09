class Solution(object):
    def translateNum1(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 将数字转换成字符串
        num_str = str(num)
        # 定义dp数组
        dp = [1, 1]
        for i in range(1, len(num_str)):
            if 10 <= int(num_str[i-1:i+1]) <= 25:
                dp.append(dp[i] + dp[i-1])
            else:
                dp.append(dp[i])
        return dp[-1]
    # 空间优化
    def translateNum2(self, num):
        num_str = str(num)
        if len(num_str) == 1:
            return 1
        p = 1
        q = 1
        r = 0
        for i in range(1, len(num_str)):
            if 10 <= int(num_str[i-1:i+1]) <= 25:
                r = p + q
            else:
                r = q
            p = q
            q = r
        return r
    # 数字取余
    # num = 12258
    def translateNum3(self, num):
        p = 1
        q = 1
        r = 0
        modd1 = num % 10   # 8
        while num:
            num = num // 10   # 1225
            modd2 = num % 10  # 5
            tmp = modd2 * 10 + modd1  # 58
            if 10 <= tmp <= 25:
                r = p + q
            else:
                r = q
            p = q
            q = r
            modd1 = modd2
        return r




if __name__ == '__main__':
    num = 1
    rel = Solution().translateNum2(num)
    print(rel)
