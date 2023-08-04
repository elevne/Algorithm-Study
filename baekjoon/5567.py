import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(0, n+1)]

relations = []
for _ in range(m):
    a, b = map(int, input().split())
    relations.append((a, b))
relations.sort()

res = 0
for r in relations:
    if r[0] == 1:
        parent[r[1]] = parent[r[0]]
    elif parent[parent[r[0]]] == 1 and parent[r[1]] != 1 and parent[r[1]] != 0:
        parent[r[1]] = 0
        res += 1
    elif parent[parent[r[1]]] == 1 and parent[r[0]] != 1 and parent[r[0]] != 0:
        parent[r[0]] = 0
        res += 1
    else:
        continue

for i in parent:
    if i == 1:
        res += 1

print(res-1)