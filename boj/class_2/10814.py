import sys

N = int(sys.stdin.readline())
mem = []
for i in range(0, N):
    age, name = sys.stdin.readline().split()
    mem.append((int(age), name))

for i in sorted(mem, key=lambda x: x[0]):
    print(i[0], i[1])
