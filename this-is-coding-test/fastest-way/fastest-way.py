# 다익스트라: 다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정 노드에서 출발하여
# 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
# 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복한다.
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해서 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3, 4 를 반복한다.

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 이동 비용 = c
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# 힙 자료구조를 이용하면 이보다 시간복잡도를 낮출 수 있다.
# 이는 특정 노드까지의 최단거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로부터 가장 거리가
# 짧은 노드를 더 빠르게 찾을 수 있다.
# 힙 자료구조는 Priority Queue 를 구현하기 위해 사용되는 자료구조 중 하나다. 스택은 가장 나중에 삽입된
# 데이터를 가장 먼저 삭제하고, 큐는 가장 먼저 삽입된 데이터를 가장 먼저 삭제한다. 우선순위 큐는 우선순위가
# 가장 높은 데이터를 가장 먼저 삭제한다는 점이 특징이다. 이러한 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을
# 때 사용한다. 파이썬에서는 우선순위 큐가 필요할 때 heapq 를 사용한다.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# 플로이드 워셜 알고리즘:
# 다익스트라 알고리즘은 한 지점에서 다른 특정 지점까지의 최단 거리를 구해야 하는 경우에 사용하는 최단 경로 알고리즘이고,
# 플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우에 사용할 수 있는 알고리즘이다.
# 이는 각 단계마다 특정한 노드 k 를 거쳐가는 경우를 확인한다. A 에서 B 로 가는 최단거리보다 A 에서 k 를 거쳐 B 로 가는
# 거리가 더 짧은지를 검사한다.

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()