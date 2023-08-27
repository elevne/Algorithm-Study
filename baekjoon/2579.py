import sys

n = int(sys.stdin.readline())

stairs = [0]

for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

# i, 0 : 연속 방문 아닌 것 / i, 1 은 연속 방문
dp = [[0, 0]] + [[0, 0] for _ in range(n)]

for i in range(1, n+1):
    if i == 1:
        dp[i][0] = stairs[i]
        dp[i][1] = stairs[i]
        continue
    dp[i][0] = max(dp[i-2]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[n]))