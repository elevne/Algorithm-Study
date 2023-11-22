import sys

input = sys.stdin.readline

n = int(input())

for k in range(n):
    class_n_score = list(map(int, input().split()))
    std_num = class_n_score[0]
    del class_n_score[0]
    class_n_score.sort()
    gap_list = [class_n_score[i+1] - class_n_score[i] for i in range(std_num-1)]
    print("Class " + str(k+1))
    max_score = class_n_score[-1]
    min_score = class_n_score[0]
    print("Max " + str(max_score) + ", Min " + str(min_score) + ", Largest gap " + str(max(gap_list)))