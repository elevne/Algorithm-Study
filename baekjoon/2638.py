import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
cheese_matrix = []
cheese_points = deque()
for i in range(N):
    row = list(map(int, input().split()))
    cheese_matrix.append(row)
    for j in range(M):
        if row[j] == 1:
            cheese_points.append((i, j))

def bfs(x, y, f, t):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]
            if _dx < 0 or _dx >= N or _dy < 0 or _dy >= M:
                continue
            elif cheese_matrix[_dx][_dy] == f:
                cheese_matrix[_dx][_dy] = t
                q.append((_dx, _dy))

bfs(0, 0, 0, -1)

result = 0
while cheese_points:
    cheese_points_len = len(cheese_points)
    cheese_points_to_delete = []
    for i in range(cheese_points_len):
        x, y = cheese_points.popleft()
        cnt = 0
        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]
            if _dx < 0 or _dx >= N or _dy < 0 or _dy >= M:
                continue
            elif cheese_matrix[_dx][_dy] == -1:
                cnt += 1

        if cnt >= 2:
            cheese_points_to_delete.append((x,y))
        else:
            cheese_points.append((x,y))
    for x, y in cheese_points_to_delete:
        cheese_matrix[x][y] = -1
        bfs(x, y, 0, -1)
    result += 1
print(result)