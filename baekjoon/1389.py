import sys
input = sys.stdin.readline

INF = 1e7

n, m = map(int, input().split())

distance_map = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    distance_map[a][b] = 1
    distance_map[b][a] = 1
for i in range(1, n+1):
    distance_map[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n+1):
        for j in range(1, n+1):
                distance_map[i][j] = min(distance_map[i][j], distance_map[i][k] + distance_map[k][j])

bacon = INF
answer = 0
for i in range(n, 0, -1):
    s = sum(distance_map[i][1:])
    if bacon >= s:
        bacon = s
        answer = i
print(answer)