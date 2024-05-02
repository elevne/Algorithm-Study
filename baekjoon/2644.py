import sys
import heapq
input = sys.stdin.readline

n = int(input())
family = [[] for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

INF = 1e9
dist = [INF] * (n+1)
dist[a] = 0

q = []
for i in family[a]:
    heapq.heappush(q, (1, i));
while q:
    d, p = heapq.heappop(q)
    if dist[p] > d:
        dist[p] = d
        for i in family[p]:
            if i != a:
                heapq.heappush(q, (d+1, i))

print(dist[b] if dist[b] != INF else -1)