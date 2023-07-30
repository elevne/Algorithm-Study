# Greedy Algorithm: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 문제 1
# N 이 주어졌을 때 K 로 나누거나, 1 을 빼는 것 중 한 가지 행동을 통해 N 을 1 이 되도록 하는 최소 횟수를 출력하라

# n, k 값 입력 받기
n, k = map(int, input().split())
# 결과값 초기화
result = 0
while True:
    target = (n // k) * k  # n 보다 작은 수 중에서 n 에서 가장 가까운 k 로 나누어 떨어지는 수
    result += (n - target)  # 위에서 구한 수를 본래 수에서 빼면 그것이 -1 을 하는 횟수
    n = target  # -1 을 모두 거치고 난 뒤의 n 값
    if n < k:
        break
    n /= k
    result += 1
result += (n - 1)  # n 이 1 이 될 때까지 -1 을 해주는 횟수 추가
print(result)


# 문제 2
# 각 자리가 숫자 (0~9) 로만 이루어진 문자열 S 가 주어졌을 때, 왼쪽에서 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기 혹은 더하기 연산자를
# 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하라

# S 입력 받기
S = input()
# 입력 받은 S 값을 int 로 쪼개 리스트에 넣기
S = list(map(int, S))
# 결과값 초기화
result = 0
for num in range(S):
    if num <= 1 or result <= 1:  # 리스트의 원소 혹은 result 가 1 이하일 때는 + 연산 진행
        result += num
    else:
        result *= num
print(result)


# 문제 3
# 한 마을에 모험가가 N 명 있다. 모험가 길드에서는 N 명을 대상으로 공포도를 측정하는데, 공포도가 X 인 모험가는 반드시 X 명 이상의 그룹을 결성하여 모험을 떠나야 한다.
# N 명의 모험가에 대한 공포도가 주어졌을 때, 모험을 떠날 수 있는 그룹 수의 최댓값을 구하라.

# n 입력 받기
n = int(input())
# 사람들의 공포도
people = list(map(int, input().split()))
people.sort()
result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수
for person in people:
    count += 1
    if count >= person:
        result += 1
        count = 0
print(result)