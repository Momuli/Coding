# 以区间[low, high]里的每个元素为根节点，构造二叉搜索树
# 以val为根节点，则[low, val-1]属于左子树,[val+1, high]属于右子树
# 以val为根节点总共可以构造的BST个数=左子树个数*右子树个数
# 可以递归求解
class Solution:
    def numTrees(self, n):
        # 备忘录
        memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # 区间[low, high]可以构造的BST个数
        def recur(low, high):
            if low >= high:
                return 1
            if memo[low][high] != 0:
                return memo[low][high]
            res = 0
            # 以[low, high]中的每个元素作为根节点构造BST
            for i in range(low, high+1):
                left_num = recur(low, i-1)
                right_num = recur(i+1, high)
                res += right_num * left_num
            memo[low][high] = res
            return res
        res = recur(1, n)
        return res

n = 3
rel = Solution().numTrees(n)
print(rel)