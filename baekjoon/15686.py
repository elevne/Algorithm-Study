import sys
import itertools
input = sys.stdin.readline

houses, chickens = [], []
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

candidates = list(itertools.combinations(chickens, m))
INF = 1e9
ans = INF
for c in candidates:
    d = 0
    # c -> 후보조합
    for h in houses:
        # h -> 집 하나하나
        min_dist = INF
        for ch in c:
            dist = abs(h[0]-ch[0]) + abs(h[1]-ch[1])
            min_dist = min(min_dist, dist)
        d += min_dist
    ans = min(ans, d)
print(ans)