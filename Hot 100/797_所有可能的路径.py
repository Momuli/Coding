# 图的遍历
class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        cur = []
        # 访问当前节点并判断当前节点是不是目标节点
        def recur(item, target):
            cur.append(item)
            if item == target:
                res.append(cur[:])
                # 一次访问item的相邻节点
            for v in graph[item]:
                recur(v, target)
            cur.pop()
        recur(0, len(graph)-1)
        return res

graph = [[1,2],[3],[3],[]]
rel = Solution().allPathsSourceTarget(graph)
print(rel)