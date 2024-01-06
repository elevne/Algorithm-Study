import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ladders = dict()
snakes = dict()
for _ in range(N):
    s, e = map(int, input().split())
    ladders[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    snakes[s] = e

queue = deque()
queue.append((1, 0))
lad_key = ladders.keys()
sn_key = snakes.keys()
visited = [0] * 101
visited[1] = 1
next_times = 0
loop = True
while loop:
    x = queue.popleft()
    cur_point = x[0]
    next_point = 0
    next_times = x[1] + 1
    for i in range(1, 7):
        next_point = cur_point + i
        while next_point in lad_key or next_point in sn_key:
            if next_point in lad_key:
                next_point = ladders.get(next_point)
            else:
                next_point = snakes.get(next_point)
        if next_point == 100:
            loop = False
            break
        else:
            if visited[next_point] == 1:
                pass
            else:
                visited[next_point] = 1
                queue.append((next_point, next_times))

print(next_times)