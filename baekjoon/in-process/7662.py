# to be added at probs-to-retry
import sys
import heapq
INF = int(1e11)
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = int(input())
    len_vir_list = 0
    del_count = 0
    for_max = []
    for_min = []
    max_del_list = []
    min_del_list = []
    for _ in range(t):
        cmd, num = input().split()
        if cmd == "I":
            heapq.heappush(for_max, -int(num))
            heapq.heappush(for_min, int(num))
            len_vir_list += 1
        if cmd == "D" and len_vir_list > del_count:
            del_count += 1
            if num == "1":
                x = heapq.heappop(for_max)
                max_del_list.append(x)
            elif num == "-1":
                x = heapq.heappop(for_min)
                min_del_list.append(x)

    print(for_max, max_del_list)
    print(min_del_list, for_min)

    if len_vir_list <= del_count:
        print("EMPTY")
    else:
        max_num = -heapq.heappop(for_max)
        min_num = heapq.heappop(for_min)
        print(str(max_num) + " " + str(min_num))

# 반례
# 1
# 9
# I 36
# I 37
# I 38
# D 1
# D 1
# I 39
# I 40
# D -1