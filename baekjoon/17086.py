import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

shark_map = []
q = deque()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            q.append((i, j))
    shark_map.append(row)


while q:
    x, y = q.popleft()
    cur_val = shark_map[x][y]

    if x-1 >= 0:
        if shark_map[x-1][y] == 0 or shark_map[x-1][y] > cur_val+1:
            shark_map[x-1][y] = cur_val + 1
            q.append((x-1, y))
    if x+1 < n:
        if shark_map[x+1][y] == 0 or shark_map[x+1][y] > cur_val+1:
            shark_map[x+1][y] = cur_val + 1
            q.append((x+1, y))
    if y-1 >= 0:
        if shark_map[x][y-1] == 0 or shark_map[x][y-1] > cur_val+1:
            shark_map[x][y-1] = cur_val + 1
            q.append((x, y-1))
    if y+1 < m:
        if shark_map[x][y+1] == 0 or shark_map[x][y+1] > cur_val+1:
            shark_map[x][y+1] = cur_val + 1
            q.append((x, y+1))
    if x-1 >= 0 and y-1 >= 0:
        if shark_map[x-1][y-1] == 0 or shark_map[x-1][y-1] > cur_val+1:
            shark_map[x-1][y-1] = cur_val + 1
            q.append((x-1, y-1))
    if x-1 >= 0 and y+1 < m:
        if shark_map[x-1][y+1] == 0 or shark_map[x-1][y+1] > cur_val+1:
            shark_map[x-1][y+1] = cur_val + 1
            q.append((x-1, y+1))
    if x+1 < n and y-1 >= 0:
        if shark_map[x+1][y-1] == 0 or shark_map[x+1][y-1] > cur_val+1:
            shark_map[x+1][y-1] = cur_val + 1
            q.append((x+1, y-1))
    if x+1 < n and y+1 < m:
        if shark_map[x+1][y+1] == 0 or shark_map[x+1][y+1] > cur_val+1:
            shark_map[x+1][y+1] = cur_val + 1
            q.append((x+1, y+1))


max_num = 0
for row in shark_map:
    max_num = max(max_num, max(row))
print(max_num-1)