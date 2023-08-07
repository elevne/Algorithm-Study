import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [i+1 for i in range(n+1)]
graph[n] = 1
deleted = [False for i in range(n+1)]

start = 0
result = []
stop_num = n
while stop_num > 0:
    cur_point = start
    cnt = 0
    while cnt < k:
        cur_point = graph[cur_point]
        if deleted[cur_point] == True:
            continue
        else:
            cnt += 1
    result.append(cur_point)
    deleted[cur_point] = True
    stop_num -= 1
    start = cur_point

res = "<" + ", ".join(list(map(str, result))) + ">"
print(res)