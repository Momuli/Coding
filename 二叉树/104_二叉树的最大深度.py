# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 分解法：最优子树高度的最大值+1
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l_l = self.maxDepth1(root.left)
        l_r = self.maxDepth1(root.right)
        rel = max(l_r, l_l)+1
        return rel
    # BFS
    def maxDepth2(self, root):
        if not root:
            return 0
        queue = [root]    # 将根节点加入列表
        depth = 0
        while queue:    # 控制树的深度
            l = len(queue)
            for _ in range(l):    # 遍历每一层的所有节点
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1    # 遍历完一层后树的深度+1
        return depth








