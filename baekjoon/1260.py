import sys
from bisect import insort
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

parent = [[] for i in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def set_graph(a, b):
    insort(parent[a], b)
    insort(parent[b], a)

dfs_result = []
def dfs(start_point):
    global parent, dfs_result
    dfs_result.append(start_point)
    visited_dfs[start_point] = True
    for other_point in parent[start_point]:
        if not visited_dfs[other_point]:
            dfs(other_point)

bfs_q = deque()
bfs_result = []
def bfs():
    global bfs_q
    while bfs_q:
        cur_point = bfs_q.popleft()
        if not visited_bfs[cur_point]:
            bfs_result.append(cur_point)
            visited_bfs[cur_point] = True
            next_points = parent[cur_point]
            for next_point in next_points:
                if not visited_bfs[next_point]:
                    bfs_q.append(next_point)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    set_graph(a, b)
bfs_q.append(v)
dfs(v)
bfs()

print(" ".join(list(map(str, dfs_result))))
print(" ".join(list(map(str, bfs_result))))

