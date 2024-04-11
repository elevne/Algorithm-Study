import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    c = int(input())
    stickers = [list(map(int, input().split())), list(map(int, input().split()))]
    for i in range(1, c):
        if i == 1:
            stickers[0][i] += stickers[1][i-1]
            stickers[1][i] += stickers[0][i-1]
        else:
            stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
    print(max(stickers[0][-1], stickers[1][-1]))