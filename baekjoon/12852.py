import sys
from collections import deque
n = int(sys.stdin.readline())
INF = 1e9
l = [(INF, 0) for _ in range(n+1)]

q = deque()
q.append((n,0))

while q:
    cur_val, cost = q.popleft()
    if cur_val == 1:
        continue
    x1 = cur_val % 2
    if x1 == 0 and l[int(cur_val/2)][0] > cost+1:
        l[int(cur_val/2)] = (cost+1, cur_val)
        q.append((int(cur_val/2), cost+1))
    x2 = cur_val % 3
    if x2 == 0 and l[int(cur_val/3)][0] > cost+1:
        l[int(cur_val/3)] = (cost+1, cur_val)
        q.append((int(cur_val/3), cost+1))
    if l[cur_val-1][0] > cost+1:
        l[cur_val-1] = (cost+1, cur_val)
        q.append((cur_val-1, cost+1))

print(l[1][0]) if n != 1 else print(0)
x = l[1][1]
course = []
course.append(1)
while x != 0:
    course.append(x)
    x = l[x][1]
course.reverse()
for y in course:
    print(y, end=" ")