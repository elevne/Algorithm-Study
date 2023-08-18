# 왜 틀리는지 모르겠음... 반례필요
# 플로이드 워셜로 다시 풀어보기 ?
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

distance_map = [[99999] * (n+1)] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    distance_map[a][b] = 1

print(distance_map)  # ...? 진짜 이유 모르겠음... 뭐지..?????

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i == j or i == k or j == k:
                continue
            if distance_map[i][j] == 1:
                continue
            d = distance_map[i][k] + distance_map[k][j]
            if d <= distance_map[i][j]:
                distance_map[i][j] = d
