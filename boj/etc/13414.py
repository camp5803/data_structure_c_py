import sys

N, K = map(int, sys.stdin.readline().split())
students = dict()

for i in range(K):
    s = sys.stdin.readline().strip()
    students[s] = i

students = sorted(students.items(), key=lambda x: x[1])

for i in range(N):
    print(students[i][0])
    if i == len(students) - 1:
        break