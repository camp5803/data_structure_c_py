import sys

N = sys.stdin.readline().strip()
result = int(N[0])

for i in range(1, len(N)):
    if int(N[i]) < 2 or result < 2:
        result += int(N[i])
    else:
        result *= int(N[i])

print(result)