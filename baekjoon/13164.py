import copy
import sys
import heapq

input = sys.stdin.readline
inf = 11e11

n, k = map(int, input().replace("\n", "").split())
people = list(map(int, input().replace("\n", "").split()))

diff_with_next = [(people[i] - people[i-1], i) for i in range(1, n)]
diff_with_next.sort(key=lambda x : x[0], reverse=True)

lines = []
for i in range(k-1):
    lines.append(diff_with_next[i][1])
lines.sort()

before = 0
after = 0
diff_sum = 0
for idx in lines:
    after = idx-1
    diff_sum += people[after] - people[before]
    before = idx
diff_sum += people[n-1]-people[before]
print(diff_sum)