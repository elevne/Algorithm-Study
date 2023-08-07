import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(i):
    other_points = nodes[i]
    for other_point in other_points:
        if not visited[other_point]:
            visited[other_point] = True
            dfs(other_point)

result = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)
