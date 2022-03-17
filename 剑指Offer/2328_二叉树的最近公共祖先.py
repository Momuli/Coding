# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []    # 存储从根节点到p的路径
        q_path = []
        self.recur(root, p, p_path)
        self.recur(root, q, q_path)
        min_l = min(len(p_path), len(q_path))
        for i in range(min_l):
            if p_path[i] == q_path[i]:
                rel = TreeNode(p_path[i])
        return rel


    def recur(self, root, p, path):
        if not root:
            return False
        path.append(root.val)
        if root.val == p.val:
            return True
        if self.recur(root.left, p, path):
            return True
        elif self.recur(root.right, p, path):
            return True
        # 如果root的左右孩子节点都不是p,那么弹出root
        else:
            path.pop()
            return False