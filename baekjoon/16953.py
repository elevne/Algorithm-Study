import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

q = deque()
answer = 1e9
q.append((a, 1))
while q:
    c, t = q.popleft()
    if c == b:
        answer = min(answer, t)
        continue
    if c*2 <= b:
        q.append((2*c, t+1))
    if 10*c + 1 <= b:
        q.append((10*c+1, t+1))

print(answer) if answer != 1e9 else print(-1)