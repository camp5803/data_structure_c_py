import sys

a = []
b = int(sys.stdin.readline())
for i in range(0, b):
    x, y = map(int, input().split(" "))
    a.append([x, y])

for i in sorted(a, key=lambda x: (x[1], x[0])):
    print(i[0], i[1])
