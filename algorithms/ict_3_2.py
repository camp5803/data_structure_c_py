import sys

N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

max_l = [num.pop(num.index(max(num))), max(num)]

result = 0
tmp = 0
for i in range(M):
    if tmp == K:
        result += max_l[1]
        tmp = 0
    else:
        result += max_l[0]
        tmp += 1

print(result)