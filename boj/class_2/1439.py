import sys

N = list(map(int, sys.stdin.readline().strip()))
z, o = 0, 0

for i in range(len(N) - 1):
    if N[i] == 1 and N[i + 1] == 0:
        o += 1
    elif N[i] == 0 and N[i + 1] == 1:
        z += 1

if N[-1] == 0:
    z += 1
else:
    o += 1

print(min(z, o))