import sys
from collections import deque

m, n = map(int, input().replace("\n", "").split())
tomatos = []
for _ in range(n):
    tomatos.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    i, j = q.popleft()
    cur_val = tomatos[i][j]
    if i > 0 and tomatos[i-1][j] == 0:
        tomatos[i-1][j] = cur_val + 1
        q.append((i-1, j))
    if i < n - 1 and tomatos[i+1][j] == 0:
        tomatos[i+1][j] = cur_val + 1
        q.append((i+1, j))
    if j > 0  and tomatos[i][j-1] == 0:
        tomatos[i][j-1] = cur_val + 1
        q.append((i, j-1))
    if j < m - 1 and tomatos[i][j+1] == 0:
        tomatos[i][j+1] = cur_val + 1
        q.append((i, j+1))

result = -1
max = 0
failed = False
for row in tomatos:
    for tom in row:
        if tom > max:
            max = tom
        if tom == 0:
            failed = True
            break

if failed:
    print(-1)
else:
    print(max-1)