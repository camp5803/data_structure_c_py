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


def dfs(grp, i, vis):
    visited[i] = True
    print(i, end=" ")
    for j in grp[i]:
        if not visited[j]:
            dfs(grp, j, vis)


dfs(graph, 1, visited)
