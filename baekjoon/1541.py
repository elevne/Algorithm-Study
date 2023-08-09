import sys

line = sys.stdin.readline()

splited_by_minus = line.split("-")

res = 0
for i in range(len(splited_by_minus)):
    x = sum(list(map(int, splited_by_minus[i].split("+"))))
    if i == 0:
        res += x
    else:
        res -= x

print(res)