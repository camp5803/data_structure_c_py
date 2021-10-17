import sys

N = int(sys.stdin.readline())
for _ in range(N):
    K = int(sys.stdin.readline())
    clothes = dict()
    for _ in range(K):
        c, t = map(str, sys.stdin.readline().split())
        if t not in clothes:
            clothes[t] = 1
        else:
            clothes[t] += 1
    result = 1
    for c in clothes:
        result *= (clothes[c] + 1)
    print(result - 1)