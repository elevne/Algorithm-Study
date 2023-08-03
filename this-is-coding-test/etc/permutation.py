# 순열: 서로 다른 n 개에서 r 개를 선택하여 일렬로 나열하는 것

import itertools

data = [1, 3, 5, 6]
for x in itertools.permutations(data, 3):
    print(list(x))

# 조합: 서로 다른 n 개에서 순서에 상관없이 서로 다른 r 개를 선택하는 것
print("==================================")
for x in itertools.combinations(data, 3):
    print(list(x))