import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


# dp
# get_left 는 지정된 칸의 왼쪽 수열 길이를 구하는 것
# left_dp 에서 본인보다 왼쪽에 있고 그 값이 본인보다 작은 것의
# get_left 저장된 값 중 최대 + 1
# get_right 도 마찬가지로
# 마지막에 모든 칸에 대해 두 개 값 더하고 -1 해준 값이 max

left_dp = [0] * (n)
right_dp = [0] * (n)

for i in range(n):
    if i == 0:
        left_dp[i] = 1
        right_dp[n-i-1] = 1
    else:
        left_max = 1
        right_max = 1
        for j in range(i):
            if nums[j] < nums[i]:
                left_max = max(left_max, left_dp[j]+1)
            if nums[n-j-1] < nums[n-i-1]:
                right_max = max(right_max, right_dp[n-j-1]+1)
        left_dp[i] = left_max
        right_dp[n-i-1] = right_max

answer = 0
for i in range(n):
    answer = max(answer, right_dp[i]+left_dp[i]-1)
print(answer)