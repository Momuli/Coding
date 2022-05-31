# 图的构建
# 存储为字典形式
graph={
        '1': ['2','3'],
        '2': ['4','5'],
        '3': ['6','7'],
        '4': ['8'],
        '5': ['8'],
        '6': ['7'],
        '7': [],
        '8': [],
        }
res = []
vis = []
# DFS
# 基于栈的深度优先遍历
def DFS1(graph, s):
    stack = []
    stack.append(s)
    vis = []   # 记录已经遍历过的点
    vis.append(s)
    while stack:
        cur = stack.pop()
        neibor = graph[cur]
        for item in neibor[::-1]:
            if item not in vis:
                vis.append(item)
                stack.append(item)
        res.append(cur)

# 递归的深度优先遍历
def DFS2(graph, s):
    if len(res) == len(graph):
        return
    res.append(s)
    vis.append(s)
    neibor = graph[s]
    for item in neibor:
        if item not in vis:
            DFS2(graph, item)

# 基于队列的广度优先遍历
def BFS(graph, s):
    queue = []
    queue.append(s)
    vis = []
    vis.append(s)
    while queue:
        cur = queue.pop(0)
        neibor = graph[cur]
        for item in neibor:
            if item not in vis:
                vis.append(item)
                queue.append(item)
        res.append(cur)

DFS1(graph, '1')
print(res)
