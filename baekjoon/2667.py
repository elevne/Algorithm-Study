import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

apt = []
q = deque()
for i in range(n):
    row = list(map(int, list(input().replace("\n", ""))))
    for j in range(n):
        if row[j] == 1:
            q.append((i, j))
    apt.append(row)

group_no = 1

def dfs(x, y):
    global group_no, apt
    if apt[x][y] == 1:
        group_no += 1
        apt[x][y] = group_no
    if x > 0 and apt[x-1][y] == 1:
        apt[x-1][y] = apt[x][y]
        dfs(x-1, y)
    if y > 0 and apt[x][y-1] == 1:
        apt[x][y-1] = apt[x][y]
        dfs(x, y-1)
    if x < n-1 and apt[x+1][y] == 1:
        apt[x+1][y] = apt[x][y]
        dfs(x+1, y)
    if y < n-1 and apt[x][y+1] == 1:
        apt[x][y+1] = apt[x][y]
        dfs(x, y+1)

while q:
    x, y = q.popleft()
    dfs(x, y)

result = []
for row in apt:
    result.extend(row)

result_set = set(result)
print(len(result_set) - 1)

result_cnt = []

for e in result_set:
    if e == 0: continue
    result_cnt.append(result.count(e))
result_cnt.sort()
for x in result_cnt:
    print(x)