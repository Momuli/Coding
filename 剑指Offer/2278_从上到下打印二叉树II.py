class TreeNode(object):
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []   # 存储二叉树所有节点
        if not root:
            return []
        queue = []  # 队列
        queue.append(root)
        while queue:
            tmp = []   # 存储每一层的节点
            for _ in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res