# class TreeNode(object):
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.rel1 = float('-inf')
        def recur(root):
            if not root:
                return float('-inf')
            left = recur(root.left)
            right = recur(root.right)
            self.rel1 = max(self.rel1, left, right, root.val+left+right)
            return max(root.val, root.val+left, root.val+right)
        rel2 = recur(root)
        return max(self.rel1, rel2)