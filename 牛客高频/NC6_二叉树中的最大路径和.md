## def maxPathSum(self, root):
### DFS递归

**思路:**
1. 考虑只有`根、左、右`三个节点的二叉树,最大和共有六种可能结果:
* 根
* 根+左
* 根+右
* 根+左+右
* 左
* 右

其中`(1)(2)(3)`中情况的结果可以向上合并
  
`(4)`不能向上合并,如果向上合并则会出现分叉,即当前根节点会被访问两次

`(6)(7)`不能向上合并,因为不包括当前根节点值,与向上的分支是断开的

2. 利用全局变量`self.rel1`记录`(4)(5)(6)`的结果
3. 定义递归函数求`(1)(2)(3)`的结果`rel2`
4. 最终结果为两种情况中的较大者`max(self.rel1, rel2)`

**代码:**
```
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.rel1 = float('-inf')
        def recur(root):
            if not root:
                return float('-inf')
            left = recur(root.left)
            right = recur(root.right)
            self.rel1 = max(self.rel1, left, right, root.val+left+right)
            return max(root.val, root.val+left, root.val+right)
        rel2 = recur(root)
        return max(self.rel1, rel2)
```