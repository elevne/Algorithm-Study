import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, p, q = map(int, input().split())
nums = {}
nums[0] = 1
def get_answer(n):
    if nums.__contains__(n):
        return nums[n]
    nums[n] = get_answer(int(n/p)) + get_answer(int(n/q))
    return nums[n]
print(get_answer(n))