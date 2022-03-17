# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 迭代
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            # p, q都在右子树
            if root.val < p.val and root.val < q.val:
                root = root.right
            # p, q都在左子树
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # p, q分别在左右子树上,root即为最近公共祖先
            else:
                break
        return root
    # 递归
    def lowestCommonAncestor2(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor2(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor2(root.right, p, q)
        return root
