# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 空树
        if not root:
            return True
        # 判断左右子树是否对称
        return self.cmpare(root.left, root.right)
    # 判断root的左右子节点是否对称
    def cmpare(self, root_l, root_r):
        # 左右子树的节点同时遍历结束
        if not root_l and not root_r:
            return True
        # 没有同时遍历结束
        if not root_l or not root_r:
            return False
        if root_r.val == root_l.val:
            return self.cmpare(root_l.left, root_r.right) and self.cmpare(root_l.right, root_r.left)
        # root_l和root_r的值不相等,一定不对称
        else:
            return False