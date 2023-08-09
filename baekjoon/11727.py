import sys

n = int(sys.stdin.readline())

tile_list = [0] * (n+1)

tile_list[1] = 1
if n != 1:
    tile_list[2] = 3

if n > 2:
    for i in range(3, n+1):
        tile_list[i] = tile_list[i-2]*2 + tile_list[i-1]
print(tile_list[n] % 10007)