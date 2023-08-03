# 선택정렬: 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 방식
# 가장 작은 것을 선택해서 앞으로 보내는 과정을 반복해서 수행하다 보면, 전체 데이터의 정렬이 이루어지게 됨
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 삽입정렬: 선택정렬은 알고리즘 문제 풀이에 사용하기에는 느리다. 이 대신 삽입정렬을 고려해볼 수 있다.
# 삽입정렬은 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 것이다.
# 숫자로 이루어진 리스트에서 왼쪽부터 순서대로 삽입정렬을 시작한다고 했을 때, 왼쪽에 있는 수가
# 자기자신보다 작거나 같아질 때까지 위치를 찾아가는 것이다.
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            else:
                break


# 퀵 정렬: 정렬 알고리즘 중 가장 많이 사용된다. 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의
# 위치를 바꾸는 방식을 사용한다. (병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘)
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터, Pivot 으로 설정한다. 피벗을 설정한 뒤, 리스트의 왼쪽에서부터
# 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다. 그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환한다.
# 이 작업을 계속 반복하게 되는데, 이 때 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈리게 되면
# 그 두 수의 위치를 바꾸는 것이 아니라 작은 데이터와 피벗의 위치를 서로 변경한다.

array = [5, 7, 8, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)


# 아래와 같이 파이썬의 장점을 살려 작성할 수도 있다
def quick_sort(array):
    if len(array) <= 1: return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# 계수정렬: 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능하다
# 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.
# 그 후, 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1 씩 증가시킨다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


# 버블정렬: 뒤에서부터 앞으로 정렬을 해나가는 구조. 맨 뒷자리에 제일 큰 값을 보내고, 제일 큰 값
# 바로 앞에 두 번쨰로 큰 값을 보내고... 배열 내의 값들을 앞뒤로 비교해서 자리를 바꾸는 작업을 계속 수행

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]