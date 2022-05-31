# 返回构造的数
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        # 返回区间[low,high]构造的BST树的列表
        def recur(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            # 以每一个元素为根节点
            for i in range(low, high+1):
                left_list = recur(low, i-1)
                right_list = recur(i+1, high)
            # 每个左BST与右BST组合
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
            return res
        res = recur(1, n)
        return res