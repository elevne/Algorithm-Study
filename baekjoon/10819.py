import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def get_sum(l):
    length = len(l)
    result = 0
    for i in range(length-1):
        result += abs(l[i]-l[i+1])
    return result

nums = list(permutations(nums, n))
answer = 0
for ns in nums:
    answer = max(answer, get_sum(ns))
print(answer)