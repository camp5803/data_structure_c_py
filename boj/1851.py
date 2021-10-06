import sys
from collections import deque

N = int(sys.stdin.readline())
choo = []
_min = 1000000
_min_idx = 0
_next_value = 0
res = 0
for i in range(N):
    choo.append(int(sys.stdin.readline()))
    if choo[i] < _min:
        _min = choo[i]
        _min_idx = i

dchoo = deque(sorted(choo))

# if _min_idx == 0:
#     for i in range(1, N):
#         if choo[i] != dchoo[i]:
#             choo[i], choo[_min_idx] = choo[_min_idx], choo[i]
#             res += (choo[i] + choo[_min_idx])
#             _min_idx = i
#             break

if _min_idx == 0:
    for i in range(N):
        if dchoo[i] != choo[_min_idx]:
            _next_value = i
            break
    for i in range(N):
        if choo[i] == dchoo[_next_value]:
            choo[i], choo[_min_idx] = choo[_min_idx], choo[i]
            res += (choo[i] + choo[_min_idx])
            _min_idx = i
            break

while _min_idx != 0:
    cnt = 0
    while True:
        if choo[_min_idx] == dchoo[_min_idx] and dchoo[_min_idx] == choo[cnt]:
            for i in range(N):
                if dchoo[i] != _min:
                    _next_value = i
                    break
            for i in range(N):
                if choo[i] == dchoo[_next_value]:
                    choo[i], choo[_min_idx] = choo[_min_idx], choo[i]
                    res += (choo[i] + choo[_min_idx])
                    _min_idx = i
                    break
        if dchoo[_min_idx] == choo[cnt]:
            choo[_min_idx], choo[cnt] = choo[cnt], choo[_min_idx]
            res += (choo[cnt] + choo[_min_idx])
            _min_idx = cnt
            break
        cnt += 1

print(res)
