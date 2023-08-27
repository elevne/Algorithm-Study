import sys

N = int(sys.stdin.readline())

def get_calender(m, n, x, y):
    k = x
    if n == y:
        while k <= m * n:
            if k % n == 0:
                return k
            else:
                k += m
    else:
        while k <= m * n:
            if k % n == y:
                return k
            else:
                k += m
    return -1

for _ in range(N):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(get_calender(m, n, x, y))