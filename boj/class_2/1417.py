import sys

N = int(sys.stdin.readline())
S = [int(sys.stdin.readline()) for i in range(N)]
cnt = 0

if N == 1:
    print(0)
    exit(0)

while True:
    if S[0] > max(S[1:]):
        break
    else:
        S[S[1:].index(max(S[1:])) + 1] -= 1
        S[0] += 1
        cnt += 1

print(cnt)