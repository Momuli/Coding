# 构建顶点有向图：每个字符当做顶点
# 构建权重有向图：存储已知的两个顶点的商
from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        # 构建图
        graph = defaultdict(set)  # graph[item]=set()
        weight = defaultdict(lambda :0)  # weight[item] = 0
        for idx, item in enumerate(equations):
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])
            weight[(item[0], item[1])] = values[idx]
            weight[(item[1], item[0])] = float(1 / values[idx])
        # 深度优先搜索
        def recur(start, end, vis):
            # 顶点不在图中
            if not start in graph or not end in graph:
                return 0
            # 边已经存在于图中
            if end in graph[start]:
                return weight[(start, end)]
            # 顶点已经访问过了
            if start in vis:
                return 0
            # 标记顶点
            vis.add(start)
            res = 0
            for item in graph[start]:
                res = recur(item, end, vis) * weight[(start, item)]
                # 备忘录
                if res != 0:
                    weight[(start, end)] = res
                    break
            # 撤销标记
            vis.remove(start)
            return res

        res = []
        for item in queries:
            temp = recur(item[0], item[1], set())
            if temp == 0:
                res.append(-1.0)
            else:
                res.append(temp)
        return res

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

rel = Solution().calcEquation(equations, values, queries)
print(rel)
