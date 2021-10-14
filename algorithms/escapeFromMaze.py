import sys


def dfs(maze, x, y, count):
    if maze[x][y] == 1:
        maze[x][y] = 0
        if x == N - 1 and y == M - 1:
            print(count)
        elif x == N - 1:
            dfs(maze, x, y + 1, count + 1)
        elif y == M - 1:
            dfs(maze, x + 1, y, count + 1)
        else:
            dfs(maze, x + 1, y, count + 1)
            dfs(maze, x, y + 1, count + 1)
    else:
        return


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
count = 0

dfs(maze, 0, 0, 1)

