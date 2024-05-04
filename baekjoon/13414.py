import sys
input = sys.stdin.readline

k, l = map(int, input().split())
waiting = {}
for i in range(l):
    id = input().replace("\n", "")
    waiting[id] = i
result = list(waiting.items())
result.sort(key=lambda x:x[1])
result = result[:k]
for a, b in result:
    print(a)