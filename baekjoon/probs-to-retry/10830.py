import copy
import sys
import time
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def multiply_matrix(m1, m2):
    global n
    new_matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for idx, x in enumerate(m1[i]):
                s += x * m2[idx][j]
            new_matrix[i].append(s%1000)
    return new_matrix


def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

    tmp = square(A, B // 2)
    if B % 2:
        return multiply_matrix(multiply_matrix(tmp, tmp), A)
    else:
        return multiply_matrix(tmp, tmp)


result = square(matrix, b)
for r in result:
    print(*r)