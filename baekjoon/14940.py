import sys
from collections import deque
input = sys.stdin.readline

def oneToMinusOne(x):
    if x == 1:
        return -1
    else:
        return x

n, m = map(int, input().split())

number_map = []
start_point = (-1, -1)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if start_point == (-1, -1) and row[j] == 2:
            start_point = (i, j)
    row = list(map(lambda x: oneToMinusOne(x), row))
    number_map.append(row)
number_map[start_point[0]][start_point[1]] = 0
q = deque()
q.append(start_point)
while q:
    cur_point = q.popleft()
    x, y = cur_point
    if x >= 1 and number_map[x-1][y] == -1:
        number_map[x-1][y] = number_map[x][y] + 1
        q.append((x-1, y))
    if y >= 1 and number_map[x][y-1] == -1:
        number_map[x][y-1] = number_map[x][y] + 1
        q.append((x, y-1))
    if x < n-1 and number_map[x+1][y] == -1:
        number_map[x+1][y] = number_map[x][y] + 1
        q.append((x+1, y))
    if y < m - 1 and number_map[x][y+1] == -1:
        number_map[x][y+1] = number_map[x][y] + 1
        q.append((x, y+1))

for l in number_map:
    print(" ".join(list(map(str, l))))