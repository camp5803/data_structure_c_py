# 수학적으로 접근했는데 답은 완전 탐색이라네요 ~
# 여긴 시간복잡도가 O(1)
import sys

N = int(sys.stdin.readline())
h = 60 * 60
r = 5 * (15 * 9 + 60) + 600

if N == 23:
    print((N - 2) * r + 3 * h)
elif N >= 13:
    print((N - 1) * r + 2 * h)
elif N >= 3:
    print(N * r + h)
else:
    print((N + 1) * r)

# OR
# 시간복잡도 O(N), N + 1회

res = 0

for i in range(N + 1):
    if '3' in str(i):
        res += h
    else:
        res += r

print(res)

# 의외로 시간복잡도가 3600(N+1)회 마찬가지로 O(N)
cnt = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

