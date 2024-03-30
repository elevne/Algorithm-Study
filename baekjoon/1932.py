import sys

input = sys.stdin.readline

n = int(input())
triangle = [[] for _ in range(n)]

for i in range(n):
    triangle[i].extend(list(map(int, input().split())))

for i in range(1, n):
    row_before = triangle[i-1]
    row = triangle[i]
    row_len = len(row)
    for j in range(row_len):
        if j == 0:
            row[j] += row_before[0]
        elif j == row_len-1:
            row[j] += row_before[j-1]
        else:
            row[j] += max(row_before[j-1], row_before[j])
print(max(triangle[-1]))