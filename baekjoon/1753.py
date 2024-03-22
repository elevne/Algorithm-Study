import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())
graph =[[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10e7
def dijkstra(i):
    distance = [INF] * (V+1)
    distance[i] = 0
    heap = []
    heapq.heappush(heap, (0, i))
    while heap:
        total_val, curr_point = heapq.heappop(heap)
        for v, w in graph[curr_point]:
            x = total_val + w
            if distance[v] > x:
                distance[v] = x
                heapq.heappush(heap, (x, v))
    return distance
result_list = dijkstra(S)
for i in range(1, len(result_list)):
    print(result_list[i]) if result_list[i] < INF else print("INF")