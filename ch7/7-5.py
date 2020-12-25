n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

# 이진 탐색의 조건 : 검색대상 배열은 오름차순으로 정렬되어 있어야 한다
n_lst = sorted(n_lst, reverse=False)


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    elif target == array[mid]:
        return mid


for tar in m_lst:
    result = binary_search(n_lst, tar, 0, n - 1)
    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

'''
5
8 3 7 9 2
3
5 7 9

8
1 5 10 65 3 7 9 2
6
6 87 9 11 10 2
'''
