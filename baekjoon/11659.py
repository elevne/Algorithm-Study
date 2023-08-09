import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums_addition_map = [0] * (n+1)

temp_addition = 0
for i in range(1, n+1):
    temp_addition += nums[i-1]
    nums_addition_map[i] = temp_addition

for _ in range(m):
    a, b = map(int, input().split())
    print(nums_addition_map[b] - nums_addition_map[a-1])