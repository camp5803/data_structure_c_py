import sys

N = int(sys.stdin.readline())
K = list(map(int, sys.stdin.readline().split()))
K.sort()

cnt = 0
res = 0

for i in range(N):
    cnt += 1
    if i <= cnt:
        res += 1
        cnt = 0

print(res)

