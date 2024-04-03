import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums_ = combinations_with_replacement(nums,m)
for p in nums_:
    for x in p:
        print(x, end=" ")
    print()