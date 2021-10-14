from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True

    while q:
        tmp = q.popleft()
        print(tmp, end=" ")
        for i in graph[tmp]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(graph, 1, visited)