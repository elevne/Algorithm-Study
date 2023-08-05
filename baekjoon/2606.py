import sys
input = sys.stdin.readline

n = int(input())
dfs_neighbors = [[] for i in range(n+1)]
dfs_visited = [False for i in range(n+1)]


m = int(input())

def dfs(x):
    dfs_visited[x] = True
    for other_point in dfs_neighbors[x]:
        if not dfs_visited[other_point]:
            dfs(other_point)

for _ in range(m):
    a, b = map(int, input().split())
    dfs_neighbors[a].append(b)
    dfs_neighbors[b].append(a)

dfs(1)
res = -1
for tf in dfs_visited:
    if tf:
        res += 1

print(res)