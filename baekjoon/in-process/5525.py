import sys

n = int(sys.stdin.readline())
pn = "I" + "OI" * n
pn_list = list(pn)

l = int(sys.stdin.readline())
s = sys.stdin.readline()
s_list = list(s)

result = 0
pn_len = len(pn)

# 첫 번째 발견한 후
# 인덱스 + 2 : 끝 인덱스 + 2 체크하기
# 고로 끝인덱스 + 1, 끝인덱스 + 2 가 각각 O, I 인지 확인만하면 됨
#  l - pn_len 값보다 작거나 같을 때 계속 이어가기

i = 0
while i <= l - pn_len:
    if s_list[i] == "I" and s_list[i+1] == "O":
        if s_list[i:i+pn_len] == pn_list:
            result += 1
            k = 0
            while True:
                if i+pn_len+k+1 >= len(s_list):
                    break
                if s_list[i+pn_len+k] == "O" and s_list[i+pn_len+k+1] == "I":
                    result += 1
                    k += 2
                else:
                    break
            i += pn_len + k
        else:
            if len(set(s_list[i+2:i+pn_len:2])) == 1 and len(set(s_list[i+1:i+pn_len:2])) == 1:
                i += pn_len
            else:
                i += 2
    else:
        i += 1

print(result)