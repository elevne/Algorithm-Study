import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

INF = 1e9
dp = [INF] * (k+1)

for i in range(1, k+1):
    if i in coins:
        dp[i] = 1
    else:
        for c in coins:
            if i-c > 0 and dp[i-c] < dp[i]:
                dp[i] = dp[i-c] + 1

answer = dp[k]
print(answer) if answer != INF else print(-1)