import sys

a, p = map(int, sys.stdin.readline().split())
visit_list = [False] * 295246

def get_next_num(n, p):
    num_str = str(n)
    num_len = len(num_str)
    num_sum = 0
    for i in range(num_len):
        n = int(num_str[i])
        num_sum += n ** p
    return num_sum

idx = 0
nums_list = []
nums_list.append(a)
visit_list[a] = True
list_len = 1
while True:
    x = nums_list[list_len-1]
    y = get_next_num(x, p)
    if visit_list[y]:
        idx = nums_list.index(y)
        break
    else:
        visit_list[y] = True
        nums_list.append(y)
        list_len += 1

print(len(nums_list[:idx]))