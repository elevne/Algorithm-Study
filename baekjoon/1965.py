import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(lambda x : [int(x), 1], input().split()))


for i in range(n):
    m = 0
    for j in range(i-1, -1, -1):
        if dp[j][0] < dp[i][0]:
            m = max(dp[j][1], m)
    dp[i][1] += m

print(max(list(map(lambda x : x[1] ,dp))))