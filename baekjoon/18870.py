import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

num_dict = dict()

ordered_nums = list(set(nums))
ordered_nums.sort()
for idx, num in enumerate(ordered_nums):
    num_dict[num] = idx

res_list = []
for n in nums:
    res_list.append(str(num_dict.get(n)))
print(" ".join(res_list))