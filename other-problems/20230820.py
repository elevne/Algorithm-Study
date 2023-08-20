# 1 번
# 자동차 제조 과정에서는 다양한 테스트를 통해 해당 자동차가 잘 만들어졌는지를 평가합니다.
# 이러한 평가지표 중 하나는 자동차의 연비입니다.
# 자동차의 연비가 높을수록 연료 소비가 적고, 더 많은 거리를 주행할 수 있으므로 이는 자동차가 잘 만들어졌는지의 지표로 사용될 수 있습니다.
# 만약 3대의 자동차를 테스트하고, 각각의 연비를 측정한다고 가정해봅시다.
# 첫 번째 자동차의 연비는 9km/L, 두 번째 자동차의 연비는 15km/L, 세 번째 자동차의 연비는 20km/L이라고 합니다. 이 경우 중앙값은 15km/L입니다.
# n대의 자동차를 새로 만들었지만 여건상 3대의 자동차에 대해서만 테스트가 가능한 상황입니다.
# n대의 자동차의 실제 연비 값이 주어졌을 때, q개의 질의에 대해 임의로 3대의 자동차를 골라 테스트하여 중앙값이 m값이 나오는 서로 다른 경우의 수를 구하는 프로그램을 작성해보세요.


import sys

input = sys.stdin.readline

n, q = map(int, input().split())
car_yb_list = list(map(int, input().split()))
car_yb_list.sort()

for _ in range(q):
    m = int(input())
    if car_yb_list.__contains__(m):
        x = car_yb_list.index(m) + 1
        list_len = len(car_yb_list)
        x_front = x - 1
        x_back = list_len - x
        print(x_front * x_back)
    else:
        print(0)

# 2 번
# Sam은 팀장님으로부터 차량이 이동 가능한 시나리오의 수를 찾으라는 업무 지시를 받았습니다.
# 이동은 숫자 0과 1로만 이루어져 있는 n x n 크기의 격자 위에서 일어납니다.
# 숫자 0은 빈 칸을 의미하며, 숫자 1은 해당 칸이 벽으로 막혀있음을 의미합니다.
# 차량은 n x n 격자 내에서 m개의 지점을 순서대로 방문하려고 합니다.
# 이 때 이동은 항상 상하좌우 중 인접한 칸으로만 이동하되 벽은 지나갈 수 없으며, 한 번 지났던 지점은 다시 방문해서는 안 됩니다.
# 이러한 조건 하에서 차량이 이동 가능한 서로 다른 가지 수를 구하는 프로그램을 작성해보세요.
# 방문해야 하는 지점의 첫 지점이 출발점이며, 마지막 지점이 도착점임에 유의합니다.
# 위의 예에서 m=3, 방문해야 하는 지점이 순서대로 (3행, 1열), (1행, 2열), (2행, 3열)이라면, 다음과 같이 5가지의 시나리오가 가능합니다.

n, m = map(int, input().split())

move_map = []

for _ in range(n):
    row = list(map(int, input().split()))
    move_map.append(row)

move_list = []

for _ in range(m):
    a, b = map(int, input().split())
    move_list.append((a, b))


# 풀이