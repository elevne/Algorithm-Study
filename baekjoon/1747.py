import sys
import math

input = sys.stdin.readline

n = int(input())


def is_symmetric(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-(i + 1)]:
            return False
    return True


def is_prime(x):
    r = int(math.sqrt(x))
    for i in range(2, r + 1):
        if x % i == 0:
            return False
    return True


if n == 1:
    n += 1
if n != 2 and n % 2 == 0:
    n += 1
while True:
    if not is_symmetric(n):
        n += 2
        continue
    if not is_prime(n):
        n += 2
        continue
    break
print(n)