a = []
b = int(input())
for i in range(0, b):
    x, y = map(int, input().split(" "))
    a.append([x, y])

for i in sorted(a, key=lambda x: (x[0], x[1])):
    print(i[0], i[1])
