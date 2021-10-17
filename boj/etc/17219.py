import sys

N, M = map(int, sys.stdin.readline().split())
keychain = dict()

for _ in range(N):
    a, p = map(str, sys.stdin.readline().split())
    keychain[a] = p

for _ in range(M):
    a = sys.stdin.readline().strip()
    print(keychain[a])
