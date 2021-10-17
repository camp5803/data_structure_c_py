import sys

N, M = map(int, sys.stdin.readline().split())
poke_book = dict()

for i in range(1, N + 1):
    poke_name = sys.stdin.readline().strip()
    poke_book[poke_name] = i

reversed_book = {v: k for k, v in poke_book.items()}

for i in range(M):
    q = sys.stdin.readline().strip()
    if q in poke_book:
        print(poke_book[q])
    elif int(q) in reversed_book:
        print(reversed_book[int(q)])

