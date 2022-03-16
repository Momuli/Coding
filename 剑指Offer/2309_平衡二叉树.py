# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 自上而下判断
    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        left_d = self.depth(root.left)
        right_d = self.depth(root.right)
        if abs(left_d-right_d) > 1:
            return False
        return self.isBalanced1(root.left) and self.isBalanced1(root.right)
    # 计算当前树的深度
    def depth(self, root):
        if not root:
            return 0
        left_dep = self.depth(root.left)
        right_dep = self.depth(root.right)
        return max(left_dep, right_dep) + 1

    # 自下而上判断
    def isBalanced2(self, root):
        def recur(root):
            if not root:
                return 0
            left_d = recur(root.left)
            if left_d == -1:
                return -1
            right_d = recur(root.right)
            if right_d == -1:
                return -1
            if abs(left_d-right_d) <= 1:
                return max(left_d, right_d) + 1
            else:
                return -1
        return recur(root) != -1