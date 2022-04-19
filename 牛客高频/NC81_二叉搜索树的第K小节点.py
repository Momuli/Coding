class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉排序树的中序遍历结果是升序排列的
class Solution:
    def KthNode(self, proot, k):
        if not proot:
            return -1
        rel = self.inorder(proot)
        if len(rel) < k or k <= 0:
            return -1
        return rel[k-1]
    def inorder(self, root):
        if not root:
            return []
        stack = [root]
        rel = []
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.append(root.right)
                stack.append(root.val)
                stack.append(root.left)
            elif isinstance(cur, int):
                rel.append(cur)
        return rel
