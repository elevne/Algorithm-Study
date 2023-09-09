# KMP 공부해서 다시 풀기
import sys
x = sys.stdin.readline().replace("\n", "")
y = sys.stdin.readline().replace("\n", "")
if y in x:
    print(1)
else:
    print(0)