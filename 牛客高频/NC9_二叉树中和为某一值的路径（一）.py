class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        return self.recur(root, sum)
    def recur(self, root, target):
        if not root:
            return False
        if root.val == target and not root.left and not root.right:
            return True
        return self.recur(root.left, target-root.val) or self.recur(root.right, target-root.val)