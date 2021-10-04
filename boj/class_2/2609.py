import sys

N, K = map(int, sys.stdin.readline().split())
result = 0

def gcd(a, b):
    t = a % b
    if t != 0:
        return gcd(b, t)
    else:
        return b

if N > K:
    result = gcd(N, K)
else:
    result = gcd(K, N)

print(result)
print((N * K) // result)