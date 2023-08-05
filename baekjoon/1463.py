import sys
input = sys.stdin.readline

n = int(input())
nums = [1e9 for i in range(n+1)]
nums[1] = 0
for idx in range(0, n+1):
    if idx == 0 or idx == 1: continue
    nums[idx] = nums[idx-1]+1
    if idx % 2 == 0:
        nums[idx] = min(nums[idx], nums[idx//2] + 1)
    if idx % 3 == 0:
        nums[idx] = min(nums[idx], nums[idx//3] + 1)


print(nums[n])
