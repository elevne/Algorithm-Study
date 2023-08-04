import sys

goal = int(sys.stdin.readline())

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
broken_count = int(sys.stdin.readline())
if broken_count != 0:
    broken_list = list(map(int, sys.stdin.readline().split()))
else:
    broken_list = []
for broken in broken_list:
    nums.remove(broken)
nums = list(map(str, nums))

ans = 0
nums_set = set(nums)
def is_sublist(s):
    return nums_set >= set(s)

found = False

nums_in_goal = list(str(goal))
if is_sublist(nums_in_goal):
    found = True
    ans += len(nums_in_goal)
if broken_count == 10:
    found = True
    ans = 9e9
i = 1
while not found:
    if i <= goal:
        goal_minus = list(str(goal-i))
        if is_sublist(goal_minus):
            found = True
            ans += len(goal_minus) + i
            break
    else:
        pass
    goal_higher = goal+i
    goal_plus = list(str(goal_higher))
    if is_sublist(goal_plus):
        found = True
        ans += len(goal_plus)+i
        break
    i += 1

ans = min(ans, abs(goal-100))

print(ans)