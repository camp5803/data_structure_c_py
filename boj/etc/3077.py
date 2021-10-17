import sys
from itertools import combinations

N = int(sys.stdin.readline())
war = {n: i for i, n in enumerate(list(map(str, sys.stdin.readline().split())), 1)}
ans = list(map(str, sys.stdin.readline().split()))

cnt = 0
for i in list(combinations(ans, 2)):
    if war[i[0]] < war[i[1]]:
        cnt += 1

print("%d/%d" % (cnt, N * (N - 1) / 2))