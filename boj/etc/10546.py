import sys

N = int(sys.stdin.readline())
runners = dict()

for _ in range(N):
    t = sys.stdin.readline().strip()
    if t in runners:
        runners[t] += 1
    else:
        runners[t] = 1

for _ in range(N - 1):
    t = sys.stdin.readline().strip()
    runners[t] -= 1

for i in runners:
    if runners[i] >= 1:
        print(i)
        break
