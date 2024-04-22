import sys
import itertools
import copy
from collections import deque
input = sys.stdin.readline
# BRUTE FORCE BFS
n, m = map(int, input().split())
lab_map = []
empty_points = []
empty_space_cnt = 0
virus_points = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 0:
            empty_points.append((i, j))
            empty_space_cnt += 1
        elif row[j] == 2:
            virus_points.append((i, j))
    lab_map.append(row)
wall_combinations = itertools.combinations(empty_points, 3)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
for combination in wall_combinations:
    lm = copy.deepcopy(lab_map)
    sc = copy.deepcopy(empty_space_cnt) - 3
    for c in combination:
        x, y = c
        lm[x][y] = 1
    q = deque()
    q.extend(virus_points)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lm[nx][ny] == 0:
                lm[nx][ny] = 2
                sc -= 1
                q.append((nx, ny))
    answer = max(answer, sc)
print(answer)