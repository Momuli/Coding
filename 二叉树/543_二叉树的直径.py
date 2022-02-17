# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_l = self.maxdepth(root.left)   # 根节点的左子树的最大深度
        max_r = self.maxdepth(root.right)   # 根节点的右子树的最大深度
        res = max_r+max_l   # 根节点的直径, 但最大直径不一定通过根节点
        # 因此整棵树的最大直径是  根节点直径, 其左子树的最大直径 以及 其右子树的最大直径中的最大者
        rel = max(res, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
        return rel

    def maxdepth(self, root):
        if not root:
            return 0
        m_l = self.maxdepth(root.left)
        m_r = self.maxdepth(root.right)
        max_len = max(m_r, m_l) + 1
        return max_len

    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return 0
        self.maxdepth2(root)
        return self.res

    def maxdepth2(self, root):
        if not root:
            return 0
        m_l = self.maxdepth2(root.left)
        m_r = self.maxdepth2(root.right)
        self.res = max(self.res, m_l+m_r)
        max_len = max(m_r, m_l) + 1
        return max_len