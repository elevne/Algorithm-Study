# to be added at probs-to-retry
# 방법이 몰까...... 고민 필요 ㅜㅜ
nums = [i**2 for i in range(1, 224)]

n = int(input())

tmp_max_num = 0
i = -1
res = 0
while n > 0:
    while tmp_max_num <= n:
        i += 1
        tmp_max_num = nums[i]
    n -= nums[i-1]
    print(i)
    res += 1
    i = -1
    tmp_max_num = 0

print(res)