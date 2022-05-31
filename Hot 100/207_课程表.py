# 图的遍历+判断是否有环
# DFS
# numCourses = 2, prerequisites = [[1,0]]
class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 构建图
        graph = self.build_graph(numCourses, prerequisites)
        # 图的遍历
        # 如果当前访问的节点已经在访问路径上，说明出现了环
        vis = [0] * numCourses
        onPath = [0] * numCourses
        self.flag = False    # 是否有环
        # 访问当前顶点
        def recur(cur):
            # 已经在路径上
            if onPath[cur] == 1:
                self.flag = True
                return
            # 没有在路径上，但是已经被访问过了或者已经找到环了
            if vis[cur] == 1 or self.flag:
                return
            vis[cur] = 1
            onPath[cur] = 1
            # 遍历cur的邻接节点
            for v in graph[cur]:
                recur(v)
            # 离开cur时撤销
            onPath[cur] = 0
        # 以每个点为起点进行访问
        for i in range(numCourses):
            recur(i)
        return not self.flag

    # 构建图的邻接表形式
    def build_graph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]  # 下标表示图中的顶点
        for item in prerequisites:
            start = item[1]
            end = item[0]
            graph[start].append(end)
        return graph

numCourses = 2
prerequisites = [[1,0],[0,1]]
rel = Solution().canFinish(numCourses, prerequisites)
print(rel)