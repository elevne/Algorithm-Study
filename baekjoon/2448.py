import math
import sys

n = int(sys.stdin.readline())
n = int(math.log2(n/3))
r1 = "  *  "
r2 = " * * "
r3 = "*****"

tri = [r1, r2, r3]

while n > 0:
    last_len = len(tri[0])
    last_row_len = len(tri)
    next_len = last_len * 2 + 1
    padding_len = int((next_len - last_len) / 2)
    padding = ""
    for i in range(padding_len):
        padding += " "
    for i in range(last_row_len):
        tri.append(tri[i] + " " + tri[i])
    for i in range(last_row_len):
        tri[i] = padding + tri[i] + padding
    n -= 1

for r in tri:
    print(r)