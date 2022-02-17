class Solution(object):
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rel_list = []
        rel_list.extend(Solution().inorderTraversal1(root.left))
        rel_list.extend([root.val])
        rel_list.extend(Solution().inorderTraversal1(root.right))
        return rel_list

    def inorderTraversal2(self, root):
        stack = []
        rel_list = []
        def add_node(root):
            while root:
                stack.extend([root])
                root = root.left
        add_node(root)
        while stack:
            cur = stack.pop()
            rel_list.extend([cur.val])
            add_node(cur.right)
        return rel_list

    def inorderTraversal3(self, root):
        res = []
        # 当不为空树
        while root:
            # 当左子树不为空时：
            if root.left:
                # 寻找x的前驱结点(x的左子树的最右边的节点)
                pre = root.left
                while (pre.right != None and pre.right != root):
                    pre = pre.right   # 找到左子树最右边的节点
                # 若pre.right不为空： 则一定指向x, pop(x), 删除有节点，x=x.right
                if pre.right:
                    res.extend([pre.right.val])
                    root = root.right
                    pre.right = None
                # 若pre.right为空,将x链接到pre.right,x=x.left
                else:
                    pre.right = root
                    root = root.left
            # 当左子树为空时：pop(x) x=x.right
            else:
                res.extend([root.val])
                root = root.right
        return res
