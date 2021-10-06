import sys

N = int(sys.stdin.readline())
mans = []

for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    mans.append((weight, height))

for i in range(N):
    cnt = 0
    for j in range(N):
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            cnt += 1
    print(cnt + 1, end=' ')