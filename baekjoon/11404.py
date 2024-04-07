import sys

input = sys.stdin.readline

n = int(input())
distance_matrix = [[1e9] * n for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    distance_matrix[a-1][b-1] = min(c, distance_matrix[a-1][b-1])

for i in range(n):
    distance_matrix[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k == i or i == j or j == k:
                continue
            elif distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
                distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

for row in distance_matrix:
    for ele in row:
        print(ele, end=" ") if ele != 1e9 else print(0, end=" ")
    print()