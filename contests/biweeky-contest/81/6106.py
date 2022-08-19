# https://leetcode.com/contest/biweekly-contest-81/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# Return the number of pairs of different nodes that are unreachable from each other.

# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.
from typing import List


def dfs(graph, node, visited):
    visited.add(node)
    count = 0
    for child in graph[node]:
        if child not in visited:
            count += dfs(graph, child, visited)
    return count + 1


def countPairs(n: int, edges: List[List[int]]) -> int:
    graph = {}
    nodes = [x for x in range(n)]
    for i in range(n):
        graph[i] = set()
    for (u, v) in edges:
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    families = []

    for child in nodes:
        if child not in visited:
            families.append(dfs(graph, child, visited))

    familyCount = len(families)
    # suffix addition for families
    suffixAdd = []
    total = 0
    for i in range(familyCount):
        total += families[familyCount - i - 1]
        suffixAdd.append(total)
    suffixAdd.reverse()
    result = 0
    for i in range(familyCount-1):
        result += families[i] * suffixAdd[i+1]
    return result


ans = countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]])
print(ans)