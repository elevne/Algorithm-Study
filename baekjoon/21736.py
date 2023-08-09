import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

campus = []
doyeon = (-1, -1)
for i in range(n):
    row = list(sys.stdin.readline())
    for j in range(len(row)):
        if row[j] == "I":
            doyeon = (i, j)
    campus.append(row)

q = deque()
q.append(doyeon)
met_person = 0
while q:
    x, y = q.popleft()
    if x > 0:
        if campus[x-1][y] == "O":
            q.append((x-1, y))
            campus[x-1][y] = "X"
        elif campus[x-1][y] == "P":
            met_person += 1
            q.append((x-1, y))
            campus[x-1][y] = "X"
        else:
            pass
    if y > 0:
        if campus[x][y-1] == "O":
            q.append((x, y-1))
            campus[x][y-1] = "X"
        elif campus[x][y-1] == "P":
            met_person += 1
            q.append((x, y-1))
            campus[x][y-1] = "X"
        else:
            pass
    if x < n-1:
        if campus[x+1][y] == "O":
            q.append((x+1, y))
            campus[x+1][y] = "X"
        elif campus[x+1][y] == "P":
            met_person += 1
            q.append((x+1, y))
            campus[x+1][y] = "X"
        else:
            pass
    if y < m-1:
        if campus[x][y+1] == "O":
            q.append((x, y+1))
            campus[x][y+1] = "X"
        elif campus[x][y+1] == "P":
            met_person += 1
            q.append((x, y+1))
            campus[x][y+1] = "X"
        else:
            pass
if met_person == 0:
    print("TT")
else:
    print(met_person)