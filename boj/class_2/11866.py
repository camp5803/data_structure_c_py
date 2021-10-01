import sys


def seek(per, pos, k):
    per_len = len(per)
    if pos + k - 1 >= per_len:
        pos = (pos + k - 1) % per_len
    else:
        pos = pos + k - 1

    if per_len == 1:
        print(per.pop(pos), end=">")
        return pos
    else:
        print(per.pop(pos), end=", ")
        return pos


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    seq = list(range(1, N + 1))
    p = 0

    print("<", end="")
    for i in range(0, N):
        p = seek(seq, p, K)