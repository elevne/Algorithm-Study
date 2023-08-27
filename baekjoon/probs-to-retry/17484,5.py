# 이 풀이는 왜 안될까?
# import sys
#
# n, m = map(int, sys.stdin.readline().replace("\n", "").split())
#
# input_map = []
#
# for i in range(n):
#     in_ = list(map(int, sys.stdin.readline().replace("\n", "").split()))
#     input_map.append(in_)
#
# prob_res = float('inf')
# moves = ["-", "=", "+"]
#
#
# def dfs(last_move, last_point, times, result):
#     global prob_res
#     if times == n:
#         prob_res = min(prob_res, result)
#         return
#
#     elif times == 1:
#         if last_point > 0:
#             dfs(moves[0], last_point - 1, times + 1, result + input_map[times][last_point - 1])
#         if last_point < m-1:
#             dfs(moves[2], last_point + 1, times + 1, result + input_map[times][last_point + 1])
#         dfs(moves[1], last_point, times + 1, result + input_map[times][last_point])
#
#     else:
#         if last_move == moves[0]:
#             dfs(moves[1], last_point, times + 1, result + input_map[times][last_point])
#             if last_point < m-1:
#                 dfs(moves[2], last_point + 1, times + 1, result + input_map[times][last_point + 1])
#         elif last_move == moves[1]:
#             if last_point > 0:
#                 dfs(moves[0], last_point - 1, times + 1, result + input_map[times][last_point - 1])
#             if last_point < m-1:
#                 dfs(moves[1], last_point + 1, times + 1, result + input_map[times][last_point + 1])
#         else:
#             dfs(moves[1], last_point, times + 1, result + input_map[times][last_point])
#             if last_point > 0:
#                 dfs(moves[0], last_point - 1, times + 1, result + input_map[times][last_point - 1])
#
#
# for i in range(m):
#     dfs(None, i, 1, input_map[0][i])
#
# print(prob_res)



import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + matrix[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i-1][j]

min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value, each)
print(min_value)