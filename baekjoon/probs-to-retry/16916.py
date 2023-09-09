import sys
x = sys.stdin.readline().replace("\n", "")
y = sys.stdin.readline().replace("\n", "")
isIn = False
for i in range(len(x)-len(y)+1):
    if x[i:i+len(y)-1] == y:
        isIn = True
print(int(isIn))