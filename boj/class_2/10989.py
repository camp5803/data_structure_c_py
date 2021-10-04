import sys

N = int(sys.stdin.readline())
check = [0] * 10000

for i in range(N):
    tmp = int(sys.stdin.readline())
    check[tmp - 1] += 1

for i in range(10000):
    if check[i] != 0:
        for j in range(check[i]):
            print(i + 1)