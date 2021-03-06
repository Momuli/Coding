# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 判断树A的子结构是否包含B
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False
        return self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
    # 判断以root为根节点的树形结构是否包含以B为根节点的树形结构,从root点开始匹配
    def recur(self, root, B):
        # 当B已经遍历结束,说明B中元素都已经和以root为根节点的树中的节点匹配上了
        if not B:
            return True
        # 以root为根节点的树已经遍历完了,
        if not root:
            return False
        # 根节点都无法匹配
        if root.val != B.val:
            return False
        # 但root与B匹配时,检查他们的子节点是否匹配
        else:
            return self.recur(root.left, B.left) and self.recur(root.right, B.right)