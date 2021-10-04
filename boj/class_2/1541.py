import sys

a = sys.stdin.readline().strip()
res = 0
ptmp = 0
stmp = ''
stat = 1

for i in a:
    if i == '-' or i == '+':
        if stat == 1:
            res += int(stmp)
            stmp = ''
        else:
            res -= int(stmp)
            stmp = ''
        if i == '-':
            stat = 0
        else:
            ptmp = 1
    else:
        stmp += i

if stat == 1:
    print(res + int(stmp))
else:
    print(res - int(stmp))