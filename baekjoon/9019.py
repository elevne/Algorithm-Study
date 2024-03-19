import sys
from collections import deque
input = sys.stdin.readline
def D(k):
    result = 2 * k
    return result % 10000 if result > 9999 else result;
def S(k):
    result = k - 1
    return 9999 if result == -1 else result
def L(k):
    if k == 0: return 0
    d1 = k // 1000
    d2 = (k % 1000) // 100
    d3 = (k % 100) // 10
    d4 = k % 10
    return d2*1000 + d3*100 + d4*10 + d1
def R(k):
    if k == 0: return 0
    d1 = k // 1000
    d2 = (k % 1000) // 100
    d3 = (k % 100) // 10
    d4 = k % 10
    return d4*1000 + d1*100 + d2*10 + d3

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.appendleft((start, ""))
    while queue:
        num, cmd = queue.pop()
        if num == end:
            print(cmd)
            break

        d = D(num)
        if visited[d]:
            pass
        else:
            queue.appendleft((d, cmd+"D"))
            visited[d] = True

        s = S(num)
        if visited[s]:
            pass
        else:
            queue.appendleft((s, cmd+"S"))
            visited[s] = True

        l = L(num)
        if visited[l]:
            pass
        else:
            queue.appendleft((l, cmd+"L"))
            visited[l] = True

        r = R(num)
        if visited[r]:
            pass
        else:
            queue.appendleft((r, cmd+"R"))
            visited[r] = True
