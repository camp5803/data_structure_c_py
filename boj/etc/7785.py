import sys

N = int(sys.stdin.readline())

log = dict()
for _ in range(N):
    n, s = map(str, sys.stdin.readline().split())
    if s == 'enter':
        log[n] = s
    elif s == 'leave':
        if n in log:
            log[n] = s

for i in dict(sorted(log.items(), key=lambda x: x[0], reverse=True)):
    if log[i] == 'enter':
        print(i)
