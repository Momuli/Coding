"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 中序遍历
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)   # 中序遍历cur的左子树
            # 目前还没有前驱节点,证明cur是头结点
            if not self.pre:
                self.head = cur
            else:
                self.pre.right, cur.left = cur, self.pre
            self.pre = cur
            dfs(cur.right)   # 中序遍历cur的右子树
        if not root:
            return
        self.pre = None  # 前驱结点
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head