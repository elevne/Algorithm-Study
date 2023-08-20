# 2 번
# Sam은 팀장님으로부터 차량이 이동 가능한 시나리오의 수를 찾으라는 업무 지시를 받았습니다.
# 이동은 숫자 0과 1로만 이루어져 있는 n x n 크기의 격자 위에서 일어납니다.
# 숫자 0은 빈 칸을 의미하며, 숫자 1은 해당 칸이 벽으로 막혀있음을 의미합니다.
# 차량은 n x n 격자 내에서 m개의 지점을 순서대로 방문하려고 합니다.
# 이 때 이동은 항상 상하좌우 중 인접한 칸으로만 이동하되 벽은 지나갈 수 없으며, 한 번 지났던 지점은 다시 방문해서는 안 됩니다.
# 이러한 조건 하에서 차량이 이동 가능한 서로 다른 가지 수를 구하는 프로그램을 작성해보세요.
# 방문해야 하는 지점의 첫 지점이 출발점이며, 마지막 지점이 도착점임에 유의합니다.
# 위의 예에서 m=3, 방문해야 하는 지점이 순서대로 (3행, 1열), (1행, 2열), (2행, 3열)이라면, 다음과 같이 5가지의 시나리오가 가능합니다.
from copy import deepcopy

n, m = map(int, input().split())

move_map = []

for _ in range(n):
    row = list(map(int, input().split()))
    move_map.append(row)

move_list = []

for _ in range(m):
    a, b = map(int, input().split())
    move_list.append((a-1, b-1))


# 풀이
result = 0
# 들러야하는 포인트들의 리스트 , 이전에 지나온 맵, 현재 위치, 도착 위치
def move_cnt(points_to_visit, past_map, cur_point, goal_point):
    global result, n
    # 현재 위치 방문처리
    x, y = cur_point
    past_map = deepcopy(past_map)
    points_to_visit = deepcopy(points_to_visit)
    past_map[x][y] = 1
    # 만약 현재 위치가 다음 목적지와 동일할 경우 그 다음 목적지로 향하게끔
    if cur_point == goal_point:
        del points_to_visit[0]
        # 방금 갔던 곳이 마지막 목적지였다면 1 을 반환
        if len(points_to_visit) == 0:
            result += 1
            return 1
        # 아직 목적지가 남아있다면
        else:
            return move_cnt(points_to_visit[:], past_map[:], cur_point, points_to_visit[0])
    # 아직 현재 위치가 다음 목적지가 아닐 경우
    else:
        if x > 0 and past_map[x-1][y] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x-1, y), goal_point)
        if y > 0 and past_map[x][y-1] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x, y-1), goal_point)
        if x < n-1 and past_map[x+1][y] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x+1, y), goal_point)
        if y < n-1 and past_map[x][y+1] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x, y+1), goal_point)


move_cnt(move_list, move_map, move_list[0], move_list[0])

print(result)