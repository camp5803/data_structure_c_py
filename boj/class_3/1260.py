import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)


def dfs(graph, pos, visited):
    visited[pos] = True
    print(pos, end=" ")
    graph[pos].sort()
    for i in graph[pos]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, pos, visited):
    q = deque([pos])
    visited[pos] = True

    while q:
        tmp = q.popleft()
        print(tmp, end=" ")
        graph[tmp].sort()
        for i in graph[tmp]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)