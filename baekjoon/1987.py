import sys
input = sys.stdin.readline

r, c = map(int, input().split())

char_map = []
char_visited = [False] * 100

for _ in range(r):
    char_map.append([x for x in input().replace("\n", "")])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_val = 0
char_visited[ord(char_map[0][0])] = True
def dfs(x, y, cnt):
    global max_val
    max_val = max(max_val, cnt)
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c:
            continue
        next_char = char_map[next_x][next_y]
        if not char_visited[ord(next_char)]:
            char_visited[ord(next_char)] = True
            dfs(next_x, next_y, cnt+1)
            char_visited[ord(next_char)] = False

dfs(0, 0, 1)
print(max_val)
