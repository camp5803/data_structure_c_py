import sys
from itertools import permutations

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
cards = []
result = []

for _ in range(N):
    cards.append(sys.stdin.readline().strip())

for i in permutations(cards, K):
    result.append(''.join(i))

print(len(set(result)))
