# 문제
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
#
# 입력
# 트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.
# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
# 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
# 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.
#
# 출력
# 첫째 줄에 트리의 지름을 출력한다.

# 포기 ㅠ
# 해설
# 이 문제를 봤을 때 플로이드 워셜이나 모든 노드에서 BFS나 DFS를 돌리고 그 중에서 최대 거리를 출력하는 로직을 생각해낼 수 있다.
# 그러나 V가 10^6까지라서 TLE가 난다
# 그래서 이 문제는 트리의 지름과 관해 증명된 성질을 이용하면 된다.
# 트리에서 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
# 이 논리의 증명은 ji.o.n.e
# 블로거분께서 아주 잘 정리해주셨으니 참고하자.
# 위 로직대로, 아무 노드에서나 BFS 또는 DFS를 한 번 돌리고 그 노드에서의 최대 거리에 있는 노드를 찾아낸다.
# 그 후, 찾아낸 노드에서 한번 더 BFS, DFS를 돌리면 그 때의 최대 거리가 곧 트리의 지름 길이이다.
# 참고로, 탐색할 때 탐색 과정에서 최대 거리와 그 때의 노드를 계속 갱신해줘도 되고,
# visited를 업뎃해주면서 탐색이 끝난 후 순회하면서 최대 값을 찾아서 최대 거리를 찾아내도 된다.
import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V + 1)]
# 2차원 리스트에 트리 저장(연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx + 1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

visited = [-1] * (V + 1)
visited[1] = 0


# 리턴 값 없음. visited에 모든 노드까지의 거리 저장
def DFS(node, dist):
    for v, d in tree[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            DFS(v, cal_dist)
    return


DFS(1, 0)
tmp = [0, 0]
# 최대 거리에 있는 노드 찾기
for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

# 찾은 노드와, 찾은 노드에서 DFS 돌려 찾은 최대 거리 노드가 지름의 양 끝점
# 이 논리의 증명은 따로 알아보자
# 논리 : 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
visited = [-1] * (V + 1)
visited[tmp[0]] = 0
DFS(tmp[0], 0)

print(max(visited))