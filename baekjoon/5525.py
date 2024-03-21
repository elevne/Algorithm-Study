import sys

n = int(sys.stdin.readline())
pn = "I" + "OI" * n
pn_len = len(pn)

l = int(sys.stdin.readline())
s = sys.stdin.readline()

result = 0


i = 0
while i <= l - pn_len:
    if s[i:i+pn_len] == pn:
        result += 1
        k = 0
        while True:
            if i+pn_len+k+1 >= len(s):
                break
            if s[i+pn_len+k] == "O" and s[i+pn_len+k+1] == "I":
                result += 1
                k += 2
            else:
                break
        i += pn_len + k
    else:
        i += 1

print(result)