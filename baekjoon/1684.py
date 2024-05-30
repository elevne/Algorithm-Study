import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

a, b = nums[0], nums[1]
m = min(abs(a), abs(b))

if any(list(map(lambda x : x == 0, nums))):
    print(0)
    exit(0)

def check(z, x):
    for n in nums[2:]:
        if n % z != x:
            return False
    return True

for i in range(m, 0, -1):
    x = a % i
    y = b % i
    if x == y:
        if check(i, x):
            print(i)
            break