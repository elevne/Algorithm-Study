import sys
from collections import deque
input = sys.stdin.readline

def is_adjacent(i, j, l):
    res = False
    for p in l:
        r, c = p
        if i == r and (j == c-1 or j == c+1):
            res = True
            break
        if j == c and (i == r-1 or i == r+1):
            res = True
            break
    return res
def get_four_block_sum_around(i, j):
    queue = deque()
    queue.append((i, j, matrix[i][j], [(i,j)]))
    res = 0
    while queue:
        r, c, val_sum, visited = queue.pop()
        if len(visited) == 4:
            res = max(res, val_sum)
        else:
            if r > 1 and (r-1, c) not in visited:
                queue.appendleft((r-1, c, val_sum+matrix[r-1][c], visited + [(r-1, c)]))
            if N - r > 1 and (r+1, c) not in visited:
                queue.appendleft((r + 1, c, val_sum + matrix[r + 1][c], visited + [(r + 1, c)]))
            if c > 1 and (r, c-1) not in visited:
                queue.appendleft((r, c-1, val_sum + matrix[r][c - 1], visited + [(r, c - 1)]))
            if M  - c > 1 and (r, c+1) not in visited:
                queue.appendleft((r, c + 1, val_sum + matrix[r][c + 1], visited + [(r, c + 1)]))
            if r >= 1 and c >= 1 and (r-1, c-1) not in visited and is_adjacent(r-1, c-1, visited):
                queue.appendleft((r-1, c-1, val_sum + matrix[r-1][c-1], visited + [(r-1, c-1)]))
            if r >= 1 and M-c > 1 and (r-1, c+1) not in visited and is_adjacent(r-1, c+1, visited):
                queue.appendleft((r-1, c+1, val_sum + matrix[r-1][c+1], visited + [(r-1, c+1)]))
            if N-r > 1 and c >= 1 and (r+1, c-1) not in visited and is_adjacent(r+1, c-1, visited):
                queue.appendleft((r+1, c-1, val_sum + matrix[r+1][c-1], visited + [(r+1, c-1)]))
            if N-r > 1 and M-c > 1 and (r+1, c+1) not in visited and is_adjacent(r+1, c+1, visited):
                queue.appendleft((r+1, c+1, val_sum + matrix[r+1][c+1], visited + [(r+1, c+1)]))
    return res

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

result = -1
for i in range(N):
    for j in range(M):
        result = max(result, get_four_block_sum_around(i, j))

print(result)