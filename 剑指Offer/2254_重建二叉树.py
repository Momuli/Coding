# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # base case
        if not preorder or not inorder:
            return
        if len(preorder) != len(inorder):
            return
        # 寻找根节点
        root = preorder[0]
        rootNode = TreeNode(root)

        # 中序遍历中root的索引
        idx = inorder.index(root)

        # 左子树的中序遍历
        left_inorder = inorder[:idx]
        # 右子树的中序遍历
        right_inorder = inorder[idx+1:]

        # 左子树的前序遍历
        left_preorder = preorder[1:idx+1]
        # 右子树的前序遍历
        right_preorder = preorder[idx+1:]

        # 递归处理左子树
        left_node = self.buildTree(left_preorder, left_inorder)
        # 递归处理右子树
        right_node = self.buildTree(right_preorder, right_inorder)

        # 向根节点添加左节点和右节点
        rootNode.left = left_node
        rootNode.right = right_node

        return rootNode