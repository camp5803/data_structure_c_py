import sys

N = list(map(str, sys.stdin.readline().strip()))
n = 0
s = []

for i in N:
    if '0' <= i <= '9':
        n += int(i)
    else:
        s.append(i)

s.sort()

print(''.join(s), end="")
if n != 0:
    print(n)