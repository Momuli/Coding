## def judgeIt(self, root):
### 二叉搜索树+完全二叉树

**思路:**
1. 二叉搜索树:
* 定义: 对于节点`A`来说,`A`的左子树上值均<`A`,`A`的右子树的值均>`A`
* 利用`从上到下递归`的方法判断每个节点的左右节点是否满足条件:

&emsp;&emsp;`base case:` `if root.val < lower or root.val > upper: return False`

&emsp; &emsp;如果当前节点满足条件: `return self.sousuo(root.left, lower, root.val) and self.sousuo(root.right, root.val, upper)`

2. 完全二叉树:
* 定义: 除了最后一层外,其余层都是满二叉树,最后一层的节点向左对齐
* 利用`BFS`按层从左向右遍历二叉树:

&emsp; &emsp;如果当前节点`A`不为空:无论`A`的左右孩子是否为空，都加入队列中

&emsp; &emsp;从头到尾遍历队列,如果队列首元素为`None`,则弹出首元素

&emsp; &emsp;如果为完全二叉树,那么`None`一定出现在队列的队尾位置,因此,如果弹出所有`None`后,队列不为空,则不是完全二叉树