class Solution(object):
    # DFS递归,自下而上交换
    # 交换root的左子树和右子树
    def mirrorTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        tmp = root.left
        root.left = self.mirrorTree1(root.right)
        root.right =self.mirrorTree1(tmp)
        return root
    # BFS,自上而下交换
    def mirrorTree2(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root