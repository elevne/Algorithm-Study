# DP
# 배열 순회
# 매 원소를 돌면서
# 이전 것 중 연결가능한 것 찾기

import sys

input = sys.stdin.readline
N = int(input())

numbers = list(map(int, input().split()))

max_len = 0
last_nums = [[] for _ in range(N+1)]
for num in numbers:
    if max_len == 0:
        last_nums[1].append(num)
        max_len += 1
    for i in range(max_len):
        tmp = max_len - i
        if any(n < num for n in last_nums[tmp]):
            if i == 0:
                max_len += 1
            last_nums[tmp+1].append(num)
            break
        elif i == max_len - 1:
            last_nums[1].append(num)
print(max_len)