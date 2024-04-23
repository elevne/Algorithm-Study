import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
cbs = list(set((itertools.combinations_with_replacement(nums, m))))
cbs.sort()
for c in cbs:
    for n in c:
        print(n, end=" ")
    print()
