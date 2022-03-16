class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义dp数组：dp[i]表示第i+1个丑数
        dp = [1]
        a = b = c = 0  # 记录索引:a表示第a个数还没有被2乘过
        nums = 1
        while len(dp) < n:
            n2 = dp[a] * 2
            n3 = dp[b] * 3
            n5 = dp[c] * 5
            dp.append(min(n2, n3, n5))
            if dp[-1] == n2:
                a += 1
            if dp[-1] == n3:
                b += 1
            if dp[-1] == n5:
                c += 1
        return dp[-1]

if __name__ == '__main__':
    n = 10
    rel = Solution().nthUglyNumber(n)
    print(rel)
