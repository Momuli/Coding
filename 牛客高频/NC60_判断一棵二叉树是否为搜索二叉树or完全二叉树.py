class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def judgeIt(self, root):
        if not root:
            return [True, True]
        rel1 = self.sousuo(root)
        rel2 = self.wanquan(root)
        return [rel1, rel2]

    def sousuo(self, root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True
        if root.val < lower or root.val > upper:
            return False
        return self.sousuo(root.left, lower, root.val) and self.sousuo(root.right, root.val, upper)

    def wanquan(self, root):
        if not root:
            return True
        queue = [root]
        while queue and queue[0]:
            cur = queue.pop(0)
            queue.append(cur.left)
            queue.append(cur.right)
        while queue and not queue[0]:
            queue.pop(0)
        return len(queue) == 0
