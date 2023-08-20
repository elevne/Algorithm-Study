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