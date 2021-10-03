import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    op = list(map(int, sys.stdin.readline().split()))
    dick = {}
    cards.sort()

    for i in cards:
        if i not in dick:
            dick[i] = 1
        else:
            dick[i] += 1

    for i in op:
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            if cards[mid] == i:
                break
            elif cards[mid] > i:
                end = mid - 1
            else:
                start = mid + 1
        if cards[mid] == i:
            print(dick[i], end=" ")
        else:
            print(0, end=" ")
