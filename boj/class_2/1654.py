k, n = map(int, input().split())
cable = []

for i in range(0, k):
    cable.append(int(input()))

start, end = 1, max(cable)

while start <= end:
    mid = (start + end) // 2
    s = 0
    for i in cable:
        s += i // mid

    if s >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)