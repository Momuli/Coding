# 递归+备忘录
class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}
        # 以num[cur]开始的子数组组合,得到目标值diff的不同表达式的数目
        def recur(cur, diff):
            # base case
            if cur == len(nums):
                if diff == 0:
                    return 1
                return 0
            key = str(cur) + '_' + str(diff)
            if key in memo:
                return memo[key]
            rel = recur(cur+1, diff-nums[cur]) + recur(cur+1, diff+nums[cur])
            memo[key] = rel
            return rel
        return recur(0, target)

nums = [1,1,1,1,1]
target = 3
rel = Solution().findTargetSumWays(nums, target)
print(rel)