import sys
from collections import deque

dq = deque()

while True:
    stat = 0
    tmp = sys.stdin.readline()[:-1]
    dq.clear()
    if tmp == '.':
        break
    for i in tmp:
        if i == '(' or i == '[':
            dq.append(i)
        if i == ')':
            if not len(dq) or dq[-1] != '(':
                stat = 1
                break
            else: dq.pop()
        elif i == ']':
            if i == ']':
                if not len(dq) or dq[-1] != '[':
                    stat = 1
                    break
                else: dq.pop()
    if len(dq) == 0 and stat == 0:
        print('yes')
    else:
        print('no')
