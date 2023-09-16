import sys
input = sys.stdin.readline
from itertools import combinations

i = 0

while True:
    input_txt = input()
    if input_txt[0] == "0":
        break

    if i:
        print()

    input_list = list(map(int, input_txt.replace("\n", "").split()))
    del input_list[0]

    combis = list(combinations(input_list, 6))
    combis2 = []
    for com in combis:
        c = [com[0], com[1], com[2], com[3], com[4], com[5]]
        c.sort()
        combis2.append(c)
    combis2.sort(key=lambda x : (x[0], x[1], x[2], x[3], x[4], x[5]))
    for c in combis2:
        res_str = str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + " " + str(c[4]) + " " + str(c[5])
        print(res_str)
    i += 1

