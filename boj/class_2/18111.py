import sys

N, K, B = map(int, sys.stdin.readline().split())
floor = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
f_sum = B


def sapjil(i):
    time = 0
    for a in range(N):
        for b in range(K):
            if floor[a][b] == i:
                continue
            elif floor[a][b] > i:
                time += (2 * (floor[a][b] - i))
            else:
                time += (i - floor[a][b])
    return time, i


for i in range(N):
    for j in range(K):
        f_sum += floor[i][j]

f_max = min(257, f_sum // (N * K) + 1)
result = [float('inf'), 0]

for i in range(0, f_max):
    t, h = sapjil(i)
    if t <= result[0]:
        result[0] = t
        if h > result[1]:
            result[1] = h

print(*result)