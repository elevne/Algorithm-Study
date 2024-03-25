import sys
import heapq
input = sys.stdin.readline

N = int(input())
INF = 1e9
distance = [INF for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    S, D, C = map(int, input().split())
    graph[S].append((D, C))
S, D = map(int, input().split())

distance[S] = 0
heap = []
heap.append((S, 0))
while heap:
    curr, total = heapq.heappop(heap)
    if distance[curr] < total:
        continue
    for next, dist_to_next in graph[curr]:
        if total + dist_to_next < distance[next]:
            distance[next] = total + dist_to_next
            heapq.heappush(heap, (next, total+dist_to_next))
print(distance[D])