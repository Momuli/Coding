# 深有优先遍历每一个节点
class Solution:
    def pathSum1(self, root, targetSum):
        if not root:
            return 0
        res = 0
        def recur(root, diff):
            if not root:
                return 0
            cur = 0
            if root.val == diff:
                cur += 1
            cur += recur(root.left, diff - root.val)
            cur += recur(root.right, diff - root.val)
            return cur
        res += recur(root, targetSum)
        res += self.pathSum1(root.left, targetSum)
        res += self.pathSum1(root.right, targetSum)
        return res
# 前缀和
    def pathSum2(self, root, targetSum):
        # preSum[item]表示前缀和为item的路径组合个数
        import collections
        preSum = collections.defaultdict(int)
        preSum[0] = 1
        # root节点之前的前缀和为cur
        def recur(root, cur):
            if not root:
                return 0
            temp = 0
            cur += root.val
            temp += preSum[cur - targetSum]
            preSum[cur] += 1
            temp += recur(root.left, cur)
            temp += recur(root.right, cur)
            preSum[cur] -= 1
            return temp
        return recur(root, 0)