class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        self.res = []
        self.cur = []
        self.path(root)
        summ = 0
        for item in self.res:
            summ += int(item)
        return summ

    # 求根节点到子节点的路径
    def path(self, root):
        if not root:
            return
        self.cur.append(str(root.val))
        if not root.val and not root.right:
            self.res.append(''.join(self.cur))
        if root.left:
            self.path(root.left)
        if root.right:
            self.path(root.right)
        self.cur.pop()