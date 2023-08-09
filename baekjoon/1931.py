import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    a, b = map(int, input().split())
    nums.append((a, b))

nums.sort(key=lambda x: (x[0], x[1]))

last_point_a = -1
last_point_b = -1
nums_to_use = []

for ab in nums:
    a, b = ab[0], ab[1]
    # 가장 최근 회의 후보와 겹치는 경우
    if a < last_point_b:
        if b < last_point_b:
            nums_to_use.append((a, b))
            nums_to_use.remove((last_point_a, last_point_b))
            last_point_a = a
            last_point_b = b
        else:
            continue
    else:
        nums_to_use.append((a, b))
        last_point_b = b
        last_point_a = a
print(len(nums_to_use))