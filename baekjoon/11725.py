import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
tree_connection = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree_connection[a].append(b)
    tree_connection[b].append(a)

parents = [0] * (n+1)
def dfs(point):
    children = tree_connection[point]
    for child in children:
        if parents[child] == 0:
            parents[child] = point
            dfs(child)
dfs(1)

for i in range(2, n+1):
    print(parents[i])