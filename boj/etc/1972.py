import sys
from itertools import combinations

while True:
    s = sys.stdin.readline().strip()
    if s == '*':
        break
    stat = 0

    for i in range(len(s) - 1):
        surprised = dict()
        if stat == 1:
            break
        for j in range(len(s) - 1 - i):
            tmp = s[j] + s[j + i + 1]
            if tmp in surprised:
                print("%s is NOT surprising." % s)
                stat = 1
                break
            surprised[tmp] = 0
    if stat == 0:
        print("%s is surprising." % s)