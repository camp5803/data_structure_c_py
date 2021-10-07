import sys

a = sys.stdin.readline().strip()

row = int(a[0]) - 1
col = ord(a[1]) - ord('a')

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
res = 0

for i in move:
    t_row = row + i[0]
    t_col = row + i[1]
    if 0 < t_row <= 8 and 0 < t_col <= 8:
        res += 1

print(res)