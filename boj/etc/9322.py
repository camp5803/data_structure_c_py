import sys

N = int(sys.stdin.readline())
for _ in range(N):
    K = int(sys.stdin.readline())
    public1 = {v: k for k, v in enumerate(list(map(str, sys.stdin.readline().split())))}
    public2 = list(map(str, sys.stdin.readline().split()))
    pattern = []

    for i in public2:
        pattern.append(public1[i])

    crypto = {k: v for k, v in zip(pattern, list(map(str, sys.stdin.readline().split())))}
    for i in sorted(crypto.items(), key=lambda x: x[0]):
        print(i[1], end=" ")
    print()
