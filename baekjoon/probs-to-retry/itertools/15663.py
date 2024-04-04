import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

ns = list(map(int, input().split()))
nums = list(set(permutations(ns, m)))
nums.sort()
for x in nums:
    for i in range(m):
        print(x[i], end=" ")
    print()
