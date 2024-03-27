import sys
input = sys.stdin.readline

N = int(input())
max_dp = []
min_dp = []
for i in range(N):
    dist = list(map(int, input().split()))
    if i == 0:
        max_dp.extend(dist)
        min_dp.extend(dist)
        continue
    min_vals = []
    max_vals = []
    for x in range(3):
        if x == 0:
            min_vals.append(min(min_dp[:2]) + dist[x])
            max_vals.append(max(max_dp[:2])+ dist[x])
        if x == 1:
            min_vals.append(min(min_dp)+ dist[x])
            max_vals.append(max(max_dp)+ dist[x])
        if x == 2:
            min_vals.append(min(min_dp[1:])+ dist[x])
            max_vals.append(max(max_dp[1:])+ dist[x])
    min_dp = min_vals
    max_dp = max_vals
print(max(max_dp), min(min_dp))