class Solution(object):
    def minCostClimbingStairs1(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n_dict = [0]*(len(cost)+1)  # 保存第n个台阶的前一个台阶的位置:dp[i]=m表示第i个台阶的上一个台阶的索引是m
        for i in range(len(cost), 1, -1):
            print(i)
            if cost[i-1] < cost[i-2]:
                n_dict[i] = i-1
            else:
                n_dict[i] = i-2
        sum = 0
        n = len(cost)
        while n > 1:
            sum = sum + cost[n_dict[n]]
            n = n_dict[n]
        return sum

    def minCostClimbingStairs2(self, cost):
        dp = [0] * (len(cost)+1)  # dp[i]表示到达第i阶的最小花费
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]

if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    rel = Solution().minCostClimbingStairs2(cost)
    print(rel)




