import sys

enum = set([str(i) for i in range(10)])
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M > 0:
    enum -= set(map(str, sys.stdin.readline().split()))

start = 100
min_case = abs(start - N)

for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] not in enum:
            break
        elif len(str(i)) - 1 == j:
            min_case = min(min_case, abs(i - N) + len(str(i)))

print(min_case)