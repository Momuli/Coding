# 维护外部变量记录比当前node节点值大的元素的累加和
class Solution:
    def convertBST(self, root):
        if not root:
            return
        self.sum = 0
        def recur(root):
            if not root:
                return
            recur(root.right)
            self.sum += root.val
            root.val = self.sum
            recur(root.left)
        recur(root)
        return root