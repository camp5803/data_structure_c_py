import sys

N = int(sys.stdin.readline())
l = []
for i in range(0, N):
    l.append(sys.stdin.readline().strip())

def VPS(vps):
    s = 0
    for c in vps:
        if c == '(':
            s += 1
        else:
            s -= 1
        if s == -1:
            return 1

    return s


for i in l:
    if VPS(i) == 0:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")

