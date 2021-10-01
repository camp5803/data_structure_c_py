N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
n.sort()


def binary_search(target, start, end, data):
    if start > end:
        return False

    mid = (start + end) // 2
    if data[mid] == target:
        return True
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(target, start, end, data)


if __name__ == '__main__':
    for i in range(0, M):
        if binary_search(m[i], 0, N - 1, n):
            print(1)
        else:
            print(0)
