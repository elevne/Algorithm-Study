import sys
import bisect
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 항상 가장 작은 두 묶음을 합치기 ?
nums.sort()
result = 0
while len(nums) > 1:
    x = nums[0] + nums[1]
    del nums[1]
    del nums[0]
    result += x
    bisect.insort(nums, x)

print(result)