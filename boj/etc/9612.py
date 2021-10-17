import sys

N = int(sys.stdin.readline())
words = dict()
m = 1
for _ in range(N):
    c = sys.stdin.readline().strip()
    if c not in words:
        words[c] = 1
    else:
        words[c] += 1
    if words[c] > m:
        m = words[c]

for i in sorted(words.items(), key=lambda x: x[0], reverse=True):
    if i[1] == m:
        print(i[0], i[1])
        break

