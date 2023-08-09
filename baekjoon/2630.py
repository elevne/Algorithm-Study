import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    row = list(map(int, input().split()))
    numbers.append(row)

cnt_blue = 0
cnt_white = 0
def countColor(l):
    cnt_b = 0
    cnt_w = 0
    for i in range(len(l)):
        for j in l[i]:
            if j == 1: cnt_b += 1
            else: cnt_w += 1
    if cnt_b == 0 or cnt_w == 0:
        return True, cnt_w == 0
    else:
        return False, False
def getCount(l):
    global cnt_blue, cnt_white
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    first_half = l[:len(l)//2]
    second_half = l[len(l)//2:]

    for row in first_half:
        q1_row = []
        q2_row = []
        for i in range(len(l)):
            if i < len(l) // 2: q1_row.append(row[i])
            else: q2_row.append(row[i])
        q1.append(q1_row)
        q2.append(q2_row)
    for row in second_half:
        q3_row = []
        q4_row = []
        for i in range(len(l)):
            if i < len(l) // 2: q3_row.append(row[i])
            else: q4_row.append(row[i])
        q3.append(q3_row)
        q4.append(q4_row)

    all_quadrants = []
    all_quadrants.append(q1)
    all_quadrants.append(q2)
    all_quadrants.append(q3)
    all_quadrants.append(q4)

    for q in all_quadrants:
        is_all_same, is_blue = countColor(q)
        if is_all_same:
            if is_blue:
                cnt_blue += 1
            else:
                cnt_white += 1
        else:
            getCount(q)
is_all_same, is_blue = countColor(numbers)
if is_all_same:
    if is_blue:
        print(0)
        print(1)
    else:
        print(1)
        print(0)
else:
    getCount(numbers)
    print(cnt_white)
    print(cnt_blue)