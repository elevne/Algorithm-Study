import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
num_combinations = permutations(nums, m)

for c in num_combinations:
    for i in range(m):
        print(c[i], end=" ")
    print()