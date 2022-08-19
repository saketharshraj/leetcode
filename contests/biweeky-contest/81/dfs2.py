def dfs(graph, node, visited=set()):
    visited.add(node)
    count = 0
    for child in graph[node]:
        if child not in visited:
            count += dfs(graph, child, visited)
    return count+1



# edges = [[1,2], [1,5], [2,3], [2,4], [2,5], [3,4], [3,6], [4,5], [4,6], [5,6]]
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
n = 6
nodes = [x for x in range(0, n+1)]
graph = {}

for i in range(0, n+1):
    graph[i] = set()

for (u, v) in edges:
    graph[u].add(v)
    graph[v].add(u)

visited = set()
families = []

for child in nodes:
    if child not in visited:
        temp = dfs(graph, child, visited)
        families.append(temp)
print(families)