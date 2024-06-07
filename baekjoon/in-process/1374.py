import heapq

n = int(input())
l = []
for _ in range(n):
    _, a, b = map(int, input().split())
    t = (a, b)
    l.append(t)

l.sort(key=lambda x: x[1])

ans_list = []
for i in range(n):
    a, b = l[i]
    if i == 0:
        heapq.heappush(ans_list, b)
        continue
    _b = heapq.heappop(ans_list)
    if _b <= a:
        heapq.heappush(ans_list, b)
    else:
        heapq.heappush(ans_list, _b)
        if len(ans_list) == 1:
            heapq.heappush(ans_list, b)
        else:
            for j in range(1, len(ans_list)):
                if ans_list[j] <= a:
                    ans_list[j] = b
                    heapq.heapify(ans_list)
                    break
                if j == len(ans_list) - 1:
                    heapq.heappush(ans_list, b)

print(len(ans_list))