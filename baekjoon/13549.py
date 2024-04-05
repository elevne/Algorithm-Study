import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
INF = 1e9
dp = [INF] * 100_001
q = deque()
q.append((n, 0))

while q:
    curr, total = q.popleft()
    if dp[curr] <= total:
        continue
    tmp = curr * 2
    dp[curr] = total
    while 0 < tmp <= 100000:
        if dp[tmp] > total:
            q.append((tmp, total))
        tmp *= 2

    if curr+1 <= 100000:
        if dp[curr+1] > total+1:
            q.append((curr+1, total+1))
    if dp[curr-1] > total+1:
        q.append((curr-1, total+1))


print(dp[k] if k != 0 else n-k)