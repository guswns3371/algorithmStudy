from bisect import bisect_left, bisect_right
import numpy as np
import random


def binary_search_mid(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search_mid(array, mid + 1, end)
    elif array[mid] > mid:
        return binary_search_mid(array, start, mid - 1)


# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)


# n = int(input())
# array = list(map(int, input().split()))

keep = 0
while keep < 5:
    n = random.randint(1, 30)
    array = np.random.randint(-40, 40, (1, n))[0]

    print("n=", n)
    print(array)
    ans = binary_search_mid(array, 0, n - 1)
    print("답[1]", end=" ")
    if ans != -1:
        keep += 1
        print(ans,"💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎")
    else:
        print(-1)

    # 이진 탐색(Binary Search) 수행
    index = binary_search(array, 0, n - 1)

    # 고정점이 없는 경우 -1 출력
    print("답[2]", end=" ")
    if index is None:
        print(-1)
    # 고정점이 있는 경우 해당 인덱스 출력
    else:
        print(index)
    print("------------------------------------------------")
    print()
