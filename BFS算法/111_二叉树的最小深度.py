# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]     # 创建队列，存入root
        depth = 1  # 最小深度为1
        # while循换控制层数(从上到下)，for循换控制每层的元素个数(从左到右)
        while queue:
            l = len(queue)  # 队列元素个数
            # 对队列中的节点进行下一层的扩展
            for i in range(l):
                cur = queue.pop(0)  # 弹出队首元素
                if (cur.left == None and cur.right == None):  # 判断当前节点是否为叶子节点
                    return depth
                # 否则，将cur的子节点加入队列
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            depth += 1

        return depth


