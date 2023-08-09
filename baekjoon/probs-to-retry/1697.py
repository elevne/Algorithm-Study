# 결국 맞추긴 했는데... 다시 한 번 해보자 그냥!
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
visited = [False] * 100001
q = deque()
q.append((n, 0))


def bfs():
    cur_point = (-1, -1)
    while cur_point[0] != m:
        cur_point = q.popleft()
        visited[cur_point[0]] = True
        if cur_point[0] < 50001:
            if not visited[cur_point[0] * 2]:
                next_point = (cur_point[0] * 2, cur_point[1]+1)
                q.append(next_point)
        if cur_point[0] < 100000:
            if not visited[cur_point[0]+1]:
                next_point_1 = (cur_point[0]+1, cur_point[1]+1)
                q.append(next_point_1)
        if cur_point[0] > 1:
            if not visited[cur_point[0]-1]:
                next_point_2 = (cur_point[0]-1, cur_point[1]+1)
                q.append(next_point_2)
    return cur_point


if n >= m:
    print(n-m)
else:
    print(bfs()[1])

