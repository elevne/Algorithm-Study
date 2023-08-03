# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 위 함수는 비효율적!
# 자연수의 약수가 가지는 특징을 파악하면 된다.
# 예를 들어 16의 약수는 1, 2, 4, 8, 16 이 있다. 이 때 모든 약수에 대하여
# 가운데 약수를 기준으로 하여 대칭적으로 2 개씩 앞뒤로 묶어서 곱하면 16 을 만들 수 있다. (가운데 약수를 기준으로 대칭)
# 그렇기 때문에 우리는 특정한 자연수 X 가 소수인지 확인하기 위해 바로 가운데 약수까지만 나누어떨어지는지 확인하면 된다.
# 다시 말해, 해당 수의 제곱근까지만 확인하면 된다.

import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 에라토스테네스의 체: 여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘
# N 보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있음
# 1. 2 부터 N 까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i 를 찾는다
# 3. 남은 수 중에서 i 의 배수를 모두 제거한다. (i 는 제거하지 않는다)
# 4. 더 이상 반복할 수 없을 때까지 2, 3 과정을 반복한다

import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")