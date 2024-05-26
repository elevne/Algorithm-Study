import sys
input = sys.stdin.readline
d = {}
for i in range(201):
    d[i-100] = 0
_ = input()
l = list(map(int, input().split()))
for n in l:
    d[n] += 1
print(d[int(input().replace('\n', ''))])