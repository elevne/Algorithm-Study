import copy
import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
chess_board_available = [[True] * n for _ in range(n)]
def is_in_diagonal_position(x1, y1, x2, y2):
    return abs(x1-x2) == abs(y1-y2)

result = 0

def dfs(i, board):
    this_row = board[i]
    for idx, e in enumerate(this_row):
        if e:
            if i == n-1:
                global result
                result += 1
                continue
            else:
                undo_list = []
                for x in range(i+1, n):
                    for y in range(n):
                        if y == idx and board[x][y]:
                            board[x][y] = False
                            undo_list.append((x,y))
                            continue
                        elif is_in_diagonal_position(i, idx, x, y) and board[x][y]:
                            board[x][y] = False
                            undo_list.append((x,y))
                            continue
                dfs(i+1, board)
                for x, y in undo_list:
                    board[x][y] = True

dfs(0, chess_board_available)
print(result)