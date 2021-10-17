import sys

A, B = map(int, sys.stdin.readline().split())
setA = set(map(int, sys.stdin.readline().split()))
setB = set(map(int, sys.stdin.readline().split()))

print(len(setA - setB) + len(setB - setA))
