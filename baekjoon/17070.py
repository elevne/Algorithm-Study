import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
matrix[0][0] = 1
matrix[0][1] = 1
if matrix[n-1][n-1] == 1:
    print(0)
    exit(0)
directions = ["→", "↘", "↓"]
answer = 0
def get_answer(x, y, past_dir):
    if x == n-1 and y == n-1:
        global answer
        answer += 1
        return
    global directions, matrix
    if past_dir == directions[0] or past_dir == directions[1]:
        if y < n-1 and matrix[x][y+1] == 0:
            matrix[x][y+1] = 1
            get_answer(x, y+1, directions[0])
            matrix[x][y+1] = 0
    if past_dir == directions[1] or past_dir == directions[2]:
        if x < n-1 and matrix[x+1][y] == 0:
            matrix[x+1][y] = 1
            get_answer(x+1, y, directions[2])
            matrix[x+1][y] = 0
    if y < n-1 and x < n-1 and matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
        matrix[x][y+1] = 1
        matrix[x+1][y] = 1
        matrix[x+1][y+1] = 1
        get_answer(x+1, y+1, directions[1])
        matrix[x][y + 1] = 0
        matrix[x + 1][y] = 0
        matrix[x + 1][y + 1] = 0

get_answer(0, 1, directions[0])
print(answer)