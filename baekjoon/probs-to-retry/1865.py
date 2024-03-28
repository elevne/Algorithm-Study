import sys

inf = 1e9
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    ans = 0
    N, M, W = map(int, input().split())
    arr = []
    distance = [inf] * (1 + N)
    for _ in range(M):
        s, e, t = map(int, input().split())
        arr.append((s, e, t))
        arr.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        arr.append((s, e, -t))

    for i in range(N):
        for now, next, cost in arr:
            if distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == N - 1:
                    ans = 1
    print('YES') if ans else print('NO')



# 접근방식은 옳았으나 조금 더 코드를 최적화할 수 있는 방법을 떠올리면 좋을 것.
def floyd(dist, n):
    for middle in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if dist[start][end]>dist[start][middle]+dist[middle][end]:
                    dist[start][end]=dist[start][middle]+dist[middle][end]
                    if start==end and dist[start][end]<0:
                        return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    # 2차원 배열
    distance_matrix = [[99999] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N+1):
        distance_matrix[i][i] = 0
    for _ in range(M):
        S, E, T = map(int, input().split())
        x = distance_matrix[S][E]
        # 두 지점을 연결하는 도로가 한 개보다 많을 수 있다
        if T < x:
            distance_matrix[S][E] = T
            distance_matrix[E][S] = T
    for _ in range(W):
        S, E, T = map(int, input().split())
        distance_matrix[S][E] = -T

    dist_dict = dict()
    for i in range(1, N+1):
        r = distance_matrix[i]
        row = dict()
        for j in range(1, N+1):
            x = r[j]
            if x != 99999:
                row[j] = x
        dist_dict[i] = row
    print("YES") if floyd(distance_matrix, N) else print("NO")
