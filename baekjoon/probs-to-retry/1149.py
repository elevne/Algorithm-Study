# 지금의 DP 방식은 문제가 있는 것을 확인
# DP 는 i-1 번째까지의 정답을 알고 있고 수정할 필요가 없어야  (거의 대체로)
# 이미 결정된 것을 다시 바꾸는 것은 더 이상 답을 보장하지 않는다. (핵심)
# 좀 더 고민해보기 => dp 세 번째 전의 값을 가져와서 거기에다 더하기

# Wrong Answer:
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# houses = []
# for _ in range(N):
#     houses.append(tuple(map(int, input().split())))
#
#
# def get_min_cost(x, houses_dp):
#     global houses
#     if x == 1:
#         first_house_idx, val = houses_dp[0]
#         second_house = houses[1]
#         tmp, tmp_idx = 99999, -1
#         for i in [0,1,2]:
#             if i == first_house_idx:
#                 continue
#             else:
#                 v = second_house[i]
#                 if v < tmp:
#                     tmp = v
#                     tmp_idx = i
#         houses_dp[1] = (tmp_idx, tmp)
#         return
#     if x >= 2:
#         idx, val = houses_dp[x-3]
#         if x-3 < 0:
#             idx = -1
#         tmp_val, tmp_i, tmp_j, tmp_k = 99999, 0, 0, 0
#         for i in [0, 1, 2]:
#             if i == idx:
#                 continue
#             for j in [0, 1, 2]:
#                 if j == i:
#                     continue
#                 for k in [0, 1, 2]:
#                     if k == j:
#                         continue
#                     else:
#                         tmp_sum = houses[x - 2][i] + houses[x-1][j] + houses[x][k]
#                         if tmp_sum < tmp_val:
#                             tmp_val = tmp_sum
#                             tmp_i = i
#                             tmp_j = j
#                             tmp_k = k
#         houses_dp[x - 2] = (tmp_i, houses[x-2][tmp_i])
#         houses_dp[x - 1] = (tmp_j, houses[x - 1][tmp_j])
#         houses_dp[x] = (tmp_k, houses[x][tmp_k])
#
#
# first_house = houses[0]
# list1 = [(0, first_house[0])] + [(-1, 999)] * (N-1)
# for i in range(1, N):
#     get_min_cost(i, list1)
# sum1 = sum(list(map(lambda x : x[1], list1)))
# print(sum1)


####### answer code -> study
import sys

input = sys.stdin.readline
n = int(input())
rgb = []
dp = [[0] * 3 for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    rgb.append(inp)
for i in range(n):
    if i == 0:
        dp[0][0] = rgb[0][0]
        dp[0][1] = rgb[0][1]
        dp[0][2] = rgb[0][2]
    else:
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][j]
            else:
                dp[i][j] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][j]
print(min(dp[n-1]))