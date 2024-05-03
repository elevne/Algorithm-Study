import sys
import heapq
input = sys.stdin.readline

n = int(input())
v = [[] for _ in range(n+1)]
INF = 1e9
dist = [(INF,None) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    v[a].append((b, c))
s, d = map(int, input().split())

q = []
stp = v[s]
dist[s] = (0, 0)
for i in stp:
    if dist[i[0]][0] > i[1]:
        dist[i[0]] = (i[1], s)
        heapq.heappush(q, (i[1],i[0]))

while q:
    val, cur = heapq.heappop(q)
    if val > dist[d][0]:
        continue
    for a, b in v[cur]:
        if dist[a][0] > val+b:
            dist[a] = (val+b, cur)
            heapq.heappush(q, (val+b, a))

ans = dist[d]
print(ans[0])
route = []
x = ans[1]
route.append(d)
route.append(x)
while x != s:
    x = dist[x][1]
    route.append(x)
route.reverse()
print(len(route))
print(" ".join(list(map(str, route))))