class Solution(object):
    def cuttingRope(self, n):
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

if __name__ == '__main__':
    n = 10
    rel = Solution().cuttingRope(n)
    print(rel)