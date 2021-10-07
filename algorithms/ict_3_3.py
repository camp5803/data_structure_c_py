import sys

N = int(sys.stdin.readline())
plan = sys.stdin.readline().split()
pos = (1, 1)


def move(drct, pos):
    if drct == 'U' and pos[0] != 1:
        return pos[0] - 1, pos[1]
    elif drct == 'D' and pos[0] != N:
        return pos[0] + 1, pos[1]
    elif drct == 'R' and pos[1] != N:
        return pos[0], pos[1] + 1
    elif drct == 'L' and pos[1] != 1:
        return pos[0], pos[1] - 1
    else:
        return pos


for i in range(len(plan)):
    pos = move(plan[i], pos)

print(*pos)