import sys
input = sys.stdin.readline

def get_distance(str_a, str_b):
    res = 0
    if str_a[0] != str_b[0]: res += 1
    if str_a[1] != str_b[1]: res += 1
    if str_a[2] != str_b[2]: res += 1
    if str_a[3] != str_b[3]: res += 1
    return res

N = int(input())
for _ in range(N):
    n = int(input())
    mbti_list = input().split()
    if n >= 48:
        print(0)
    else:
        result = 999
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    tmp = get_distance(mbti_list[i], mbti_list[j]) + get_distance(mbti_list[j], mbti_list[k]) + get_distance(mbti_list[i], mbti_list[k])
                    result = min(result, tmp)
        print(result)
