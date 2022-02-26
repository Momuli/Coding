class Solution(object):
    # 带备忘录的自上而下的递归(超时)
    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.hash_d = dict()
        if root in self.hash_d:
            return self.hash_d[root]
        # 当前节点被抢
        do_root = root.val + ((self.rob1(root.left.left) + self.rob1(root.left.right)) if root.left else 0) + ((self.rob(root.right.left) + self.rob(root.right.right)) if root.right else 0)
        # 当前节点不抢
        not_root = self.rob1(root.left)+self.rob1(root.right)
        res = max(do_root, not_root)
        self.hash_d[root] = res
        return res

    # 基于后序遍历的动态规划
    def rob2(self, root):
        if not root:
            return 0
        res_n, res_s = self.max_pro(root)
        return max(res_n, res_s)

    def max_pro(self, root):
        if not root:
            return 0, 0
        ln, ls = self.max_pro(root.left)
        rn, rs = self.max_pro(root.right)
        root_n = max(ln, ls) + max(rn, rs)
        root_s = root.val + rn + ln
        return root_n, root_s