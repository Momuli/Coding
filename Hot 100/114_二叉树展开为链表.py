# 将左右子树展开为链表
# 将右子链表链接到左子链表的尾部
# 根节点的右指针指向左子链表
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 将左右子树展平为链表
        self.flatten(root.left)
        self.flatten(root.right)
        # 左右子链表分配指针
        left = root.left
        right = root.right
        # 根节点右指针指向左子链表
        root.right = left
        root.left = None
        # 找左子链表的末尾节点
        p = root
        while p.right:
            p = p.right
        p.right = right