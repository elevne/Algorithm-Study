import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
result_list = combinations_with_replacement(nums, m)
for r in result_list:
    for t in range(m):
        print(r[t], end=" ")
    print()