import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # BFS
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        queue = collections.deque([root])   # 队列存储节点
        res = []   # 存储最终的序列化结果
        while queue:
            cur = queue.popleft()
            if cur:
                res.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                queue.append(None)
        return res

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        queue = collections.deque()
        root = TreeNode(data[0])
        queue.append(root)
        i = 1
        while queue:
            cur = queue.popleft()
            if data[i] != None:
                cur.left = TreeNode(data[i])
                queue.append(cur.left)
            i += 1
            if data[i] != None:
                cur.right = TreeNode(data[i])
                queue.append(cur.right)
            i += 1
        return root