import sys

n = int(sys.stdin.readline())

ans_list = [0] * (n+1)
ans_list[1] = 1
if n > 1:
    ans_list[2] = 2
for i in range(3, n+1):
    ans_list[i] = (ans_list[i-2] + ans_list[i-1])

print(ans_list[n] % 10007)