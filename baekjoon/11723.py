import sys
input = sys.stdin.readline

n = int(input())
S = [0] * 21
for _ in range(n):
    input_str = input().replace("\n","")
    if input_str == "empty" or input_str == "all":
        cmd = input_str
        pass
    else:
        cmd, num = input_str.split()
        num = int(num)

    if cmd == "add":
        if S[num] == 0:
            S[num] = 1
    elif cmd == "remove":
        if S[num] != 0:
            S[num] = 0
    elif cmd == "check":
        if S[num] == 0:
            print(0)
        else:
            print(1)
    elif cmd == "toggle":
        if S[num] == 0:
            S[num] = 1
        else:
            S[num] = 0
    elif cmd == "empty":
        for i in range(1, 21):
            S[i] = 0
    elif cmd == "all":
        for i in range(1, 21):
            S[i] = 1