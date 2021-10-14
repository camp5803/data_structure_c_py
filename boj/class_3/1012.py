import sys
sys.setrecursionlimit(100000)


def dfs(graph, x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x + 1, y)
        dfs(graph, x, y + 1)
        return True
    return False


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * N for _ in range(M)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if dfs(field, i, j):
                count += 1

    print(count)