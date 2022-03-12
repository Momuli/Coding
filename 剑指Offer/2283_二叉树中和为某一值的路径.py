# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        res = []   # 存储所有满足条件的路径
        cur = []   # 存储当前路径
        def recur(root1, target1):
            if not root1:
                return
            cur.append(root1.val)
            target1 = target1 - root1.val
            # 当root1为叶子结点并且等于target1时,此条路径搜索完毕
            if target1 == 0 and not root1.left and not root1.right:
                res.append(list(cur))
            # 递归处理子节点
            recur(root1.left, target1)
            recur(root1.right, target1)
            cur.pop()
        recur(root, target)
        return res