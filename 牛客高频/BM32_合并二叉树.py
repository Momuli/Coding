class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS
    def mergeTrees1(self , t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees1(t1.left, t2.left)
        t1.right = self.mergeTrees1(t1.right, t2.right)
        return t1

    # BFS
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        que = [(t1, t2)]
        # que只添加t1和t2对应位置都存在的节点
        while que:
            cur1, cur2 = que.pop(0)
            cur1.val = cur1.val + cur2.val
            # 左子节点
            if cur1.left and cur2.left:
                que.append((cur1.left, cur2.left))
            elif not cur1:
                cur1.left = cur2.left
            if cur1.right and cur2.right:
                que.append((cur1.right, cur2.right))
            elif not cur1.right:
                cur1.right = cur2.right
        return t1

