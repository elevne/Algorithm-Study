import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = 10e7
graph = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
transit1, transit2 = map(int, input().split())

def dijkstra(i):
    heap = []
    distance_list = [INF] * (N+1)
    distance_list[i] = 0
    heapq.heappush(heap, (i, 0))
    while heap:
        curr_point, total_dist = heapq.heappop(heap)
        for next_point, dist_to_next in enumerate(graph[curr_point]):
            if next_point == 0 or dist_to_next == INF:
                continue
            if distance_list[next_point] > total_dist + dist_to_next:
                distance_list[next_point] = total_dist + dist_to_next
                heapq.heappush(heap, (next_point, total_dist + dist_to_next))
    return distance_list

from_starting_point = dijkstra(1)
from_first_transit = dijkstra(transit1)
from_second_transit = dijkstra(transit2)

result = min(from_starting_point[transit1] + from_first_transit[transit2] + from_second_transit[N],
          from_starting_point[transit2] + from_second_transit[transit1] + from_first_transit[N])
print(result) if result < INF else print(-1)