import sys


def fact(n):
    if n == 0 : return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    n = fact(N)
    r = fact(K) * fact(N - K)
    print(n // r)
