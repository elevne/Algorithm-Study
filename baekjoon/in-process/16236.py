import sys
input = sys.stdin.readline

n = int(input())

baby_shark = (-1, -1)

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            baby_shark = (i, j)

