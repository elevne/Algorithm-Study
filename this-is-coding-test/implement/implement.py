# 구현 문제: 알고리즘 자체는 간단하지만 코드가 길어지거나 작성하기 까다로운 문제들
# e.g., 모든 경우의 수를 다 계산하는 완전탐색 (Brute Forcing) / 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 시뮬레이션 유형

# 문제 1
# 여행가 A 는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
# 가장 위 좌표는 (1,1) 이며, 가장 아래 좌표는 (N,N) 이다. 여행가 A 는 상, 하, 좌, 우 방향으로 이동할 수
# 있으며 시작 좌표는 항상 (1,1) 이다. 여행가 A 가 이동할 계획이 적힌 계획서를 보고 이동한 후의 좌표를 구한다.
# 상, 하, 좌, 우 는 U, D, R, L 로 표현되며 정사각형 공간을 벗어나는 움직임은 무시된다.

n = int(input())
x, y = 1, 1  # x, y 좌표
plans = input().split()
# 좌, 우, 상, 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
# 이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)


# 문제 2
# 정수 N 이 입력되면 00 시 00 분 00 초부터 N 시 59 분 59 초까지의 모든 시각 중에서 3 이 하나라도 포함되는 모든
# 경우의 수를 구하는 프로그램을 작성한다.

n = int(input())
result = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1
print(result)