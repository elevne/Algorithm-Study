import bisect

def binary_insertion_sort(a):
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
        # insort(a, x, lo, hi)

print('이진 삽입 정렬')
num = int(input('원소 수 입력: '))
x = [None] * num    # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print(''.join(str(x)))
binary_insertion_sort(x)
print(''.join(str(x)))