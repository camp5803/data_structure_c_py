import sys

S = sys.stdin.readline().strip()
cnt = 0
res = ''


def printString(count, dot, result):
    if count % 2 != 0:
        print(-1)
        exit(0)
    while count != 0:
        q = count // 4
        result += 'AAAA' * q
        count -= q * 4
        d = count // 2
        result += 'BB' * d
        count -= d * 2
    if dot:
        result += '.'
    return result, count


for i in S:
    if i != '.':
        cnt += 1
    if i == '.':
        res, cnt = printString(cnt, 1, res)

res, cnt = printString(cnt, 0, res)
print(res)