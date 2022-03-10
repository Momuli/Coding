class Solution(object):
    def cuttingRope1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义dp数组:dp[i]表示长度为i的绳子剪成m段的最大乘积
        dp = [0 for _ in range(n+1)]
        # base case
        dp[2] = 1   # 2 = 1 + 1
        # 绳子的长度从3开始
        for i in range(3, n+1):
            # j表示第一下剪的长度,第一次剪1m对乘积无益,因此从2m开始剪
            for j in range(2, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

    # 由定理证明:将绳子以3等分为多段时,乘积最大
    def cuttingRope2(self, n):
        # 按原理来说当绳子长度为3时,不剪短乘积最大(1*3),但题目要求剪的段数m>1
        if n <= 3:
            return n-1
        p = n // 3  # n总共可以分为p个长度为3的段
        q = n % 3   # n不能被3整除时,剩余最后一段绳子的长度(0,1,2)
        if q == 0:
            return 3**p
        elif q == 1:
            return 3**(p-1)*4   # 当最后一段长度为1时,可以和倒数第二段合并拆分为2*2 (2*2>1*3)
        elif q == 2:
            return 3**p*2
if __name__ == '__main__':
    n = 10
    rel = Solution().cuttingRope2(n)
    print(rel)