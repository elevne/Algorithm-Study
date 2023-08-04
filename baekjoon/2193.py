import sys

# n = 1 : 1    1
# n = 2 : 1     10
# n = 3 : 2    101 100   sum ~(i-2) + 1
# n = 4 : 3  1010 1001 1000   sum ~(i-2) + 1
# n = 5 : 5  10101 10100 10010 10001 10000
# n = 6 : 3 + 2 + 1 + 1

n = int(sys.stdin.readline())

num_list = [0] * 91
num_list[1] = 1
num_list[2] = 1
num_list[3] = 2
num_list[4] = 3
def get2ChinSoo(n):
    if n > 4:
        for i in range(5, n+1, 1):
            x = 1
            for j in range(1, i-1):
                x += num_list[j]
            num_list[i] = x
    return num_list[n]

print(get2ChinSoo(n))