# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # DFS
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_dep = self.maxDepth1(root.left)
        right_dep = self.maxDepth1(root.right)
        res = max(left_dep, right_dep) + 1
        return res
    # BFS
    def maxDepth2(self, root):
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth