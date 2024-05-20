import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int ,input().split()))

i, j, total = 0, 0, nums[0]
answer = 1e9
while i < n and j < n:
    if total >= s:
        answer = min(answer, j-i+1)
        total -= nums[i]
        i += 1
    elif total < s:
        j += 1
        if j == n:
            break
        total += nums[j]

print(answer if answer != 1e9 else 0)