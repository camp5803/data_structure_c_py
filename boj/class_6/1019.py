import sys
from collections import deque

N = int(sys.stdin.readline())
num_list = [0] * 10
tmp = N
cnt = 1

for i in range(len(str(N))):
    tmp = int(str(N // 10) + '9')
    sub = tmp - N
    for j in range(10): num_list[j] += (N // 10 + 1) * cnt
    for k in range(10 - sub, 10): num_list[k] -= cnt
    for l in list(str(N)[:-1]):
        num_list[int(l)] -= sub * cnt

    num_list[0] -= cnt
    cnt *= 10
    N //= 10

print(*num_list)