import sys

input = sys.stdin.readline
N = int(input())
adjacency_matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    adjacency_matrix.append(row)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adjacency_matrix[i][j] == 0 and adjacency_matrix[i][k] == 1 and adjacency_matrix[k][j] == 1:
                adjacency_matrix[i][j] = 1

for row in adjacency_matrix:
    print(" ".join(map(str, row)))