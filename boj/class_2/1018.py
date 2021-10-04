import sys

N, K = map(int, sys.stdin.readline().split())
board = []
cnt = 0
res = 64
for i in range(N):
    board.append([i for i in sys.stdin.readline().strip()])

for f in range(N - 7):
    for s in range(K - 7):
        tmp1 = 0
        tmp2 = 0
        for i in range(f, f + 8):
            for j in range(s, s + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == 'B':
                        tmp1 += 1
                    if board[i][j] == 'W':
                        tmp2 += 1
                else:
                    if board[i][j] == 'W':
                        tmp1 += 1
                    if board[i][j] == 'B':
                        tmp2 += 1
        if tmp1 < tmp2:
            if tmp1 < res:
                res = tmp1
        else:
            if tmp2 < res:
                res = tmp2

print(res)