import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    dnote1 = {i: 0 for i in note1}
    M = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        if note2[i] in dnote1:
            print(1)
        else:
            print(0)
