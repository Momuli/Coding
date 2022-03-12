import sys
class Solution(object):
    # 递归法
    def verifyPostorder1(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        # 判断区间[i,j]中的序列是否满足BST的结构  [左子树|右子树|根]
        def recur(i, j):
            # 当区间只有一个元素时:满足要求
            if i >= j:
                return True
            p = i
            # 寻找右子树后序遍历的首元素
            while postorder[p] < postorder[j]:
                p += 1
            m = p   # 右子树后序遍历首元素的索引
            # 右子树的所有元素都大于根节点
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m-1) and recur(m, j-1)

    # 根据序列构造BST
    def verifyPostorder2(self, postorder):
        def build(postorder, ma, mi):
            if not postorder:
                return
            val = postorder[-1]  # 根节点的值
            # 不满足二叉搜索树结构
            if not mi < val < ma:
                return
            postorder.pop()   # 弹出根节点
            build(postorder, ma, val)  # 右子树
            build(postorder, val, mi)  # 左子树
        build(postorder, sys.maxsize, -sys.maxsize)
        return not postorder