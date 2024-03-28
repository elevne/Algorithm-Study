# 1167 번이랑 동일한 유형
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [-1 for _ in range(N+1)]
def DFS(current_node, dist_sum):
    for next_node, dist_to_next_node in graph[current_node]:
        if visited[next_node] == -1:
            dist_total = dist_sum + dist_to_next_node
            visited[next_node] = dist_total
            DFS(next_node, dist_total)
    return

visited[1] = 0
DFS(1, 0)

max_node = 0
max_tmp = 0
for i in range(1, N+1):
    if visited[i] > max_tmp:
        max_node = i
        max_tmp = visited[i]

visited = [-1 for _ in range(N+1)]
visited[max_node] = 0
DFS(max_node, 0)
print(max(visited))