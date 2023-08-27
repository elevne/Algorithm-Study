import sys

n, m = map(int, sys.stdin.readline().split())

input_map = []

for i in range(n):
    in_ = list(map(int, sys.stdin.readline().split()))
    input_map.append(in_)

prob_res = float('inf')
combinations = []
moves = ["-", "=", "+"]


def get_combinations(last_move, last_point, times, result):
    global prob_res
    if times == n:
        prob_res = min(prob_res, result)
        return

    elif times == 1:
        if last_point > 0:
            get_combinations(moves[0], last_point-1, times+1, result+input_map[times][last_point-1])
        if last_point < m-1:
            get_combinations(moves[2], last_point+1, times+1, result+input_map[times][last_point+1])
        get_combinations(moves[1], last_point, times+1, result+input_map[times][last_point])

    else:
        if last_move == moves[0]:
            get_combinations(moves[1], last_point, times+1, result+input_map[times][last_point])
            if last_point < m-1:
                get_combinations(moves[2], last_point+1, times+1, result+input_map[times][last_point+1])
        elif last_move == moves[1]:
            if last_point > 0:
                get_combinations(moves[0], last_point-1, times+1, result+input_map[times][last_point-1])
            if last_point < m-1:
                get_combinations(moves[1], last_point+1, times+1, result+input_map[times][last_point+1])
        else:
            get_combinations(moves[1], last_point, times+1, result+input_map[times][last_point])
            if last_point > 0:
                get_combinations(moves[0], last_point-1, times+1, result+input_map[times][last_point-1])


for i in range(m):
    get_combinations(None, i, 1, input_map[0][i])

print(prob_res)
