import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(1, len(row)):
        row[i] += row[i-1]
    nums.append(row)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for i in range(x2-x1+1):
        if y1 >= 2:
            result += (nums[x1-1+i][y2-1] - nums[x1-1+i][y1-2])
        else:
            result += nums[x1-1+i][y2-1]
    print(result)