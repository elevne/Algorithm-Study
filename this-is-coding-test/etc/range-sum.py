# 접두사 합: 각 쿼리에 대해 구간합을 빠르게 계산하기 위해서는 N 개의 수의 위치 각각에 대해서
# 접두사 합을 미리 구해 놓으면 된다.
# 1. N 개의 수에 대하여 접두사 합을 계산하여 배열 P 에 저장한다
# 2. 매 M 개의 쿼리 정보 [L, R] 을 확인할 때, 구간 합은 P[R]-P[L-1] 이다
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])