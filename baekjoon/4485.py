import sys
from collections import deque

i = 0
while True:
    i += 1
    n = int(sys.stdin.readline())
    if n == 0: break
    route = []
    q = deque()
    for _ in range(n):
        route.append(list(map(int, sys.stdin.readline().replace("\n", "").split())))
    weights = [[99999] * n for i in range(n)]

    weights[0][0] = route[0][0]
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        if x > 0 and weights[x-1][y] > weights[x][y] + route[x-1][y]:
            weights[x-1][y] = weights[x][y] + route[x-1][y]
            q.append((x-1, y))
        if x < n-1 and weights[x+1][y] > weights[x][y] + route[x+1][y]:
            weights[x+1][y] = weights[x][y] + route[x+1][y]
            q.append((x+1, y))
        if y > 0 and weights[x][y-1] > weights[x][y] + route[x][y-1]:
            weights[x][y-1] = weights[x][y] + route[x][y-1]
            q.append((x, y-1))
        if y < n-1 and weights[x][y+1] > weights[x][y] + route[x][y+1]:
            weights[x][y+1] = weights[x][y] + route[x][y+1]
            q.append((x, y+1))
    result = weights[n-1][n-1]
    print("Problem "+str(i)+": "+str(result))