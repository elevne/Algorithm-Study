import sys
import heapq
input = sys.stdin.readline

n = int(input())

numbers = []

def is_positive(x):
    if x > 0:
        return True
    else:
        return False

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(numbers) == 0:
            print(0)
        else:
            num, is_num_positive = heapq.heappop(numbers)
            if is_num_positive:
                print(num)
            else:
                print(-num)
    else:
        heapq.heappush(numbers, (abs(x), is_positive(x)))
