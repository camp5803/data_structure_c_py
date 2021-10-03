import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    res = 0
    tmp = N - len(str(N)) * 9
    if tmp < 0:
        tmp = 1

    for i in range(tmp, N + 1):
        num_list = list(map(int, str(i)))
        res = i + sum(num_list)
        if res == N:
            print(i)
            exit(0)

        if i == N:
            print(0)
