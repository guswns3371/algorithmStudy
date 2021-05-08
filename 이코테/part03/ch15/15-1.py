from bisect import bisect_left, bisect_right
import random

import numpy as np


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


# n, x = map(int, input().split())
# array = list(map(int, input().split()))
# n, x = random.randint(1, 10 ** 6), random.randint(-int(1e9), int(1e9))

keep = True
while keep:
    n, x = random.randint(1, 100), random.randint(-20, 20)
    array = np.random.randint(-20, 20, (1, n))[0]
    array = np.append(array, np.random.randint(-20, 20, (1, n))[0])
    array = np.append(array, np.random.randint(-20, 20, (1, n))[0])
    array = np.append(array, np.random.randint(-20, 20, (1, n))[0])
    array = np.append(array, np.random.randint(-20, 20, (1, n))[0])
    array = np.append(array, np.random.randint(-20, 20, (1, n))[0])
    array.sort()
    print(n*6, x)
    print(array)
    ans = bisect_right(array, x) - bisect_left(array, x)
    print("답[1]", end=" ")
    if ans == 0:
        print(-1)
    else:
        keep = False
        print(ans)

    # n, x = map(int, input().split())  # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
    # array = list(map(int, input().split()))  # 전체 데이터 입력 받기

    # 값이 [x, x] 범위에 있는 데이터의 개수 계산
    count = count_by_range(array, x, x)

    print("답[2]", end=" ")
    # 값이 x인 원소가 존재하지 않는다면
    if count == 0:
        print(-1)
    # 값이 x인 원소가 존재한다면
    else:
        keep = False
        print(count)

    print("--------------------")
    print()
