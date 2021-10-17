import sys

N, P = map(int, sys.stdin.readline().split())
W, L, G = map(int, sys.stdin.readline().split())
score = 0
players = dict()
for _ in range(P):
    p, w = map(str, sys.stdin.readline().split())
    players[p] = w

for _ in range(N):
    p = sys.stdin.readline().strip()
    if p not in players or players[p] == 'L':
        score -= L
        if score < 0:
            score = 0
    else:
        score += W
    if score >= G:
        print("I AM NOT IRONMAN!!")
        exit(0)

print("I AM IRONMAN!!")