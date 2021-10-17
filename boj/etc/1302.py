import sys

N = int(sys.stdin.readline())
books = dict()

for _ in range(N):
    b = sys.stdin.readline().strip()
    if b in books:
        books[b] += 1
    else:
        books[b] = 1

for i in sorted(books):
    if books[i] == max(books.values()):
        print(i)
        break
