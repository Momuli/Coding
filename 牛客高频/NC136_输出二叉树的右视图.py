class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, xianxu, zhongxu):
        root = self.restruction(xianxu, zhongxu)
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            len_q = len(queue)
            path = []
            for _ in range(len_q):
                cur = queue.pop(0)
                path.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(path[-1])
        return res

    def restruction(self, pre, mid):
        if not mid or not pre or len(mid) != len(pre):
            return []
        root = TreeNode(pre[0])
        idx = mid.index(root.val)

        left_pre = pre[1:idx + 1]
        left_mid = mid[:idx]

        right_pre = pre[idx + 1:]
        right_mid = mid[idx + 1:]

        root.left = self.restruction(left_pre, left_mid)
        root.right = self.restruction(right_pre, right_mid)
        return root