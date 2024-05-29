import sys

n = int(sys.stdin.readline())
cnt = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

current_page = 1

to9 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
to99 = list(map(lambda x : x*10 + 10, to9))
to99[0] += 9 - 10
to999 =  list(map(lambda x : x*10 + 100, to99))
to999[0] += 18 - 100 + (9*9)
to9999 = list(map(lambda x : x * 10 + 1000, to999))
to9999[0] += 3*9 - 1000 + (99*9)
to99999 = list(map(lambda x : x * 10 + 10000, to9999))
to99999[0] += 4*9 - 10000 + (999*9)
to999999 = list(map(lambda x : x * 10 + 100000, to9999))
to999999[0] += 5*9 - 100000 + (9999*9)
to9999999 = list(map(lambda x : x * 10 + 1000000, to99999))
to9999999[0] += 6*9 - 1000000 + (99999*9)
to99999999 = list(map(lambda x : x * 10 + 10000000, to999999))
to99999999[0] += 7*9 - 10000000 + (999999*9)


print(to99999999)


to9999 = [1890+3*9, 3000+1, 3000+1, 3000+1, 3000+1, 3000+1, 3000+1, 3000+1, 3000+1, 3000+1]
# to99999 -> to9999 * 10, 1~9 +=1, 0 += 4*9


while True:
    if n < 10:
        for i in range(1, n+1):
            cnt[i] += 1
        break
    elif 10 <= n < 100:
        m = n // 10
        for i in range(m):
            if i > 0:
                cnt[i] += 10
            for idx, c in enumerate(to9):
                cnt[idx] += c
            cnt[0] += 1
        l = n % 10
        cnt[m] += l+1
        n = l
    elif 100 <= n < 1000:
        m = n // 100
        for i in range(m):
            if i > 0:
                cnt[i] += 100
            for idx, c in enumerate(to99):
                cnt[idx] += c
            cnt[0] += 11
        l = n % 100
        cnt[m] += l+10
        n = l

print(cnt)