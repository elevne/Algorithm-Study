import sys

s = sys.stdin.readline().replace("\n", "")
slen = len(s)
res = []
for i in range(1, slen+1):
    x = 0
    while x+i <=  slen:
        res.append(s[x:x+i])
        x += 1
print(len(set(res)))