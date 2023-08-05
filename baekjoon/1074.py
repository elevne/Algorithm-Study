import sys

N, r, c = map(int, sys.stdin.readline().replace("\n", "").split())

result = 0
def quadrant(n):
    global result, r, c
    quadrant_num = 0
    moves_in_quadrant = 2 ** (2*n-2)
    half_len = 2 ** (n-1)
    if r < half_len and c < half_len:
        quadrant_num = 1
    elif c >= half_len and r < half_len:
        quadrant_num = 2
        result += (quadrant_num-1) * moves_in_quadrant
        c -= half_len
    elif c < half_len and r >= half_len:
        quadrant_num = 3
        result += (quadrant_num-1) * moves_in_quadrant
        r -= half_len
    else:
        quadrant_num = 4
        result += (quadrant_num-1) * moves_in_quadrant
        r -= half_len
        c -= half_len
    if n == 1:
        return
    else:
        quadrant(n-1)
quadrant(N)
print(result)