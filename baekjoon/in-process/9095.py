# 풀긴 했는데 다시 보자

import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import product, permutations
# 1 : 1
# 2 : 11 2
# 3 : 111 21 3
# 4 : 1111 112 22 31
# 5 : 11111 2111 23 221 311

# 2 가 1 개 ~ n 개 인 경우
# 3 이 1 개 & 2 는 안쓰는 경우 계산

result_set = []
def count_combination(n):
    result_set.append(([1] * n))
    nd2 = n // 2
    for i in range(1, nd2+1):
        temp_list = [2] * i
        n_nd2 = n - (i*2)
        n_nd2_nd3 = n_nd2 // 3
        in_list_for_3 = []
        for j in range(n_nd2_nd3+1):
            temp_list2 = [3] * j
            for k in range(n_nd2-j*3):
                temp_list2.append(1)
            in_list_for_3.append(temp_list2)
        for inners in in_list_for_3:
            tmp_temp_list = deepcopy(temp_list)
            tmp_temp_list.extend(inners)
            result_set.append(tmp_temp_list)
    nd3 = n // 3
    for i in range(1, nd3+1):
        temp_list = [3] * i
        n_nd3 = n - (3*i)
        ones = [1] * n_nd3
        temp_list.extend(ones)
        result_set.append(temp_list)

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
def get_count(l):
    ones = 0
    twos = 0
    thress = 0
    for num in l:
        if num == 1: ones += 1
        elif num == 2: twos += 1
        else: thress += 1
    length = len(l)
    return factorial(length) // (factorial(ones)*factorial(twos)*factorial(thress))


def get_answer(x):
    result = 0
    count_combination(x)
    for a in result_set:
        result += get_count(a)
    print(result)
    result_set.clear()

n = int(input())
for _ in range(n):
    x = int(input())
    get_answer(x)