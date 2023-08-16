# 왜 틀리는지 모르겠음... 반례필요
# 플로이드 워셜로 다시 풀어보기 ?
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

relationships = [[] for _ in range(n + 1)]

distance_map = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    relationships[a].append(b)
    relationships[b].append(a)

def dfs(start_point, current_point, cnt):
    next_points = relationships[current_point]
    for next_point in next_points:
        d = distance_map[start_point][next_point]
        if (d == 0 or d > cnt) and next_point != start_point:
            distance_map[start_point][next_point] = cnt
            distance_map[next_point][start_point] = cnt
            dfs(start_point, next_point, cnt+1)

for i in range(1, n+1):
    dfs(i, i, 1)

kb_nums = [99999]

for i in range(1, n+1):
    distances = distance_map[i]
    kb_num = sum(distances)
    kb_nums.append(kb_num)

min_num = min(kb_nums)
print(distance_map)
print(kb_nums.index(min_num))