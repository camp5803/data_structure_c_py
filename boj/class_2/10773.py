import sys
from collections import deque

N = int(sys.stdin.readline())
money = deque()

for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        money.pop()
    else:
        money.append(tmp)

print(sum(money))