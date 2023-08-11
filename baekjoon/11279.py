import sys
import heapq

n = int(sys.stdin.readline())

numbers = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(-heapq.heappop(numbers))
    else:
        heapq.heappush(numbers, -x)