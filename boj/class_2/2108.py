import sys
from collections import Counter


def mode(num_list):
    a = Counter(num_list).most_common()
    if len(a) > 1 and a[0][1] == a[1][1]:
        return a[1][0]
    else:
        return a[0][0]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    num = []

    for i in range(0, N):
        num.append(int(sys.stdin.readline()))

    num.sort()

    print(round(sum(num) / N))
    print(num[N // 2])
    print(mode(num))
    print(num[-1] - num[0])
