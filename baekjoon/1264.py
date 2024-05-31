import sys

m = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", 'U']
while True:
    s = sys.stdin.readline().replace("\n", "")
    if s == '#':
        exit(0)
    l = len(s)
    cnt = 0
    for i in range(l):
        if s[i] in m:
            cnt += 1
    print(cnt)
