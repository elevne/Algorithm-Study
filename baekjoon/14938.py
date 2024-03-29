import sys

input = sys.stdin.readline

INF = 1e9
n, m, r = map(int, input().split())
items = [0]
items.extend(list(map(int, input().split())))
dist_matrix = [[INF if i != j else 0 for j in range(n+1)] for i in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    dist_matrix[a][b] = c
    dist_matrix[b][a] = c

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == j or k == i or k == j:
                continue
            new_dist = dist_matrix[i][k] + dist_matrix[k][j]
            if new_dist < dist_matrix[i][j]:
                dist_matrix[i][j] = new_dist

max_val = 0
for i in range(1, n+1):
    start_on_i = dist_matrix[i]
    tmp_max = 0
    for j in range(1, n+1):
        if start_on_i[j] <= m:
            tmp_max += items[j]
    max_val = max(tmp_max, max_val)
print(max_val)