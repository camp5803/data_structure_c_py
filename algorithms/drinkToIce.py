import sys


def dfs(drink, x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if drink[x][y] == 0:
        drink[x][y] = 1
        dfs(drink, x - 1, y)
        dfs(drink, x, y - 1)
        dfs(drink, x + 1, y)
        dfs(drink, x, y + 1)
        return True
    return False


N, M = map(int, sys.stdin.readline().split())
drink = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if dfs(drink, i, j):
            count += 1

print(count)