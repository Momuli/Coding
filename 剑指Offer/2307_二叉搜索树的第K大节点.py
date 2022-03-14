# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 中序遍历
    def kthLargest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def recur(cur):
            if not cur:
                return
            recur(cur.left)
            res.append(cur.val)
            recur(cur.right)
        if not root:
            return
        recur(root)
        if k <= len(res):
            return res[-k]
        else:
            return None
    # 中序遍历的倒序
    def kthLargest2(self, root, k):
        def recur(cur):
            if not cur:
                return
            recur(cur.right)
            if self.K == 0:
                return
            self.K -= 1
            if self.K == 0:
                self.res = cur.val
            recur(cur.left)

        if not root:
            return
        self.K = k
        recur(root)
        return self.res