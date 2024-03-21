# 포기...
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M, X = map(int, input().split())
#
# distance_matrix = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     st, ed, ti = map(int, input().split())
#     distance_matrix[st].append((ed, ti))
#
# queue = deque()
# for i in range(1, N+1):
#     if i != X:
#         queue.append((i, i, False, 0))
#
# real_distance_matrix = [[9999999] * (N+1) for _ in range(N+1)]
# while queue:
#     start, cur, passed_party, total = queue.pop()
#     if not passed_party and cur == X:
#         for tup in distance_matrix[cur]:
#             if total+tup[1] < real_distance_matrix[start][tup[0]]:
#                 real_distance_matrix[start][tup[0]] = total+tup[1]
#                 queue.appendleft((start, tup[0], True, total+tup[1]))
#     if passed_party and cur == start:
#         pass
#         # if total < real_distance_matrix[start][cur]:
#         #     real_distance_matrix[start][cur] = total
#     else:
#         for tup in distance_matrix[cur]:
#             if total+tup[1] < real_distance_matrix[start][tup[0]]:
#                 real_distance_matrix[start][tup[0]] = total+tup[1]
#                 queue.appendleft((start, tup[0], passed_party, total+tup[1]))
# result = 0
# for i in range(1, N+1):
#     if i == X:
#         continue
#     result = max(result, real_distance_matrix[i][i])
# print(result)
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)