from itertools import combinations
p = []
for _ in range(9):
    p.append(int(input()))

cb = list(combinations(p, 7))
answer = None
for c in cb:
    if sum(c) == 100:
        answer = list(c)

answer.sort()
for nj in answer:
    print(nj)