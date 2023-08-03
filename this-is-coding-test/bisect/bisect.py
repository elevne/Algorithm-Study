# 순차탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

# 재귀함수 이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 반복문 이진탐색
array = list()
target = 0
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 파이썬에서는 위와 같이 직접 구현할 필요 없이, 이진탐색 라이브러리를 사용할 수 있다.
# bisect 라는 기본 모듈에서 bisect_left, bisect_right 라는 메소드를 import 해서 사용한다.
# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a 에 x 를 삽입할 가장 왼쪽 인덱스 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a 에 x 를 삽입할 가장 오른쪽 인덱스 반환