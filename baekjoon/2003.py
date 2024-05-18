import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
i, j = 0, 0
for i in range(n):
    s = nums[i]
    if s == m:
        answer += 1
        continue
    for j in range(i+1, n):
        s += nums[j]
        if s == m:
            answer += 1
        elif s > m:
            break

print(answer)
