import sys
input = sys.stdin.readline

n = int(input())
ht = dict()
for _ in range(n):
    x = int(input())
    if ht.__contains__(x):
        ht[x] += 1
    else:
        ht[x] = 1

max_val = 0
max_key = 0
it = list(ht.items())
it.sort(key=lambda x:x[0])
for x, y in it:
    if y > max_val:
        max_val = y
        max_key = x
print(max_key)