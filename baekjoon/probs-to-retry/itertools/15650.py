# 라이브러리 사용법 기억하자!
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]
combis = combinations(nums, m)
for x in combis:
    for n in x:
        print(n, end=" ")
    print()