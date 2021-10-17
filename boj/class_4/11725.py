import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for i in range(1, N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            parent[i] = start
            dfs(graph, i, visited)


dfs(graph, 1, visited)
for i in range(2, N + 1):
    print(parent[i])