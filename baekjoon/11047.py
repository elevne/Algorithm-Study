import sys
input = sys.stdin.readline

n, k = map(int, input().split())
units = []
for _ in range(n):
    units.append(int(input()))

res = 0
units = units[::-1]
for unit in units:
    if k // unit > 0:
        res += (k // unit)
        k %= unit
print(res)