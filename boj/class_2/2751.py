import sys

N = int(sys.stdin.readline())
num_list = []
for i in range(0, N):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    sys.stdout.write(str(i)+'\n')