import sys

len_list = [0 for _ in range(101)]
len_list[1] = 1
len_list[2] = 1
len_list[3] = 1
len_list[4] = 2
len_list[5] = 2

for i in range(6, 101):
    len_list[i] = len_list[i-1] + len_list[i-5]

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(len_list[x])