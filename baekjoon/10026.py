import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())

color_map = []
color_map_for_sy = []
for _ in range(n):
    row = list(input())
    color_map.append(row)
    color_map_for_sy.append(deepcopy(row))

completed = "X"

def dfs_color(x, y, is_sy):
    if is_sy:
        cur_color = color_map_for_sy[x][y]
        color_map_for_sy[x][y] = completed
    else:
        cur_color = color_map[x][y]
        color_map[x][y] = completed

    if cur_color == "X":
        pass
    else:
        if is_sy:
            if x > 0 and is_same_color(cur_color, color_map_for_sy[x-1][y], is_sy):
                dfs_color(x-1, y, is_sy)
            if y > 0 and is_same_color(cur_color, color_map_for_sy[x][y-1], is_sy):
                dfs_color(x, y-1, is_sy)
            if x < n-1 and is_same_color(cur_color, color_map_for_sy[x+1][y], is_sy):
                dfs_color(x+1, y, is_sy)
            if y < n-1 and is_same_color(cur_color, color_map_for_sy[x][y+1], is_sy):
                dfs_color(x, y+1, is_sy)
        else:
            if x > 0 and is_same_color(cur_color, color_map[x-1][y], is_sy):
                dfs_color(x-1, y, is_sy)
            if y > 0 and is_same_color(cur_color, color_map[x][y-1], is_sy):
                dfs_color(x, y-1, is_sy)
            if x < n-1 and is_same_color(cur_color, color_map[x+1][y], is_sy):
                dfs_color(x+1, y, is_sy)
            if y < n-1 and is_same_color(cur_color, color_map[x][y+1], is_sy):
                dfs_color(x, y+1, is_sy)


def is_same_color(current_color, next_color, is_sy):
    if next_color == "X":
        return False
    else:
        if is_sy:
            if current_color == "B":
                return current_color == next_color
            else:
                return next_color != "B"
        else:
            return current_color == next_color


normal = 0
sy = 0

for i in range(n):
    for j in range(n):
        if color_map[i][j] == "X":
            pass
        else:
            dfs_color(i, j, False)
            normal += 1

        if color_map_for_sy[i][j] == "X":
            pass
        else:
            dfs_color(i, j, True)
            sy += 1

print(str(normal), str(sy))