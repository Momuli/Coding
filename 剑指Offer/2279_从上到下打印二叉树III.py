from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        depth = 1
        # 奇数行从左到右打印,偶数行从右向左打印
        while queue:
            tmp = deque()
            for _ in range(len(queue)):
                cur = queue.popleft()
                if depth % 2 == 0:
                    tmp.appendleft(cur.val)
                else:
                    tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(list(tmp))
        return res