# 서로소 집합: 공통 원소가 없는 두 집합 -> 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현한다.
# 서로소 집합 정보가 주어졌을 때 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘은 아래와 같다.
# 1. union (합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B 를 확인한다.
# 1.1 A 와 B 의 루트 노드 A', B' 를 각각 찾는다.
# 1.2 A' 를 B' 의 부모 노드로 설정한다 (B' 가 A' 를 가리키도록 하는 것)
# 2. 모든 union (합집합) 연산을 처리할 때까지 1 번 과정을 반복한다.

# 예제 (6, 4), (1, 4), (2, 3), (2, 4), (5, 6) 입력이 주어졌을 때 서로소 집합으로 묶기

# 특정 원소가 속한 집합 찾는 함수
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
# union 연산을 각각 수행
cycle = False  # 사이클 발생 여부
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        continue
    else:
        union_parent(parent, a, b)
if cycle:
    print("사이클 발생")
# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end="")
print()
# 부모 테이블 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end="")



# 신장 트리: 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘: 다양한 문제 상황에서 가능한 한 최소한의 비용으로 신장 트리를 찾아야 하는 경우가 있다.
# e.g. n 개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우
# 2 개의 도시 A, B 를 선택했을 때, 도시 A 에서 도시 B 로 이동하는 경로가 반드시 존재하도록 도로를 설치하고자 한다.
# 모든 도시를 연결할 때, 최소한의 비용으로 연결하려면 어떤 알고리즘을 사용해야 할까?
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# 2.1 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
# 2.2 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
# 3. 모든 간선에 대해 2 번의 과정을 반복한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int(input().split()))
parent = [0] * (v+1)
# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(v+1):
    parent[i] = i
# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
# 간선을 비용 순으로 정렬
edges.sort()
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)



# 위상 정렬: 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# e.g. 선수과목을 고려한 학습 순서 설정
# 진입차수: 특정한 노드롤 들어오는 간선의 개수 (해당 과목의 선수과목의 수)
# 1. 진입차수가 0 인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
# 2.1 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
# 2.2 새롭게 진입차수가 0 이 된 노드를 큐에 넣는다

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 처음 시작할 때는 진입차수가 0 인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft();
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")
topology_sort()