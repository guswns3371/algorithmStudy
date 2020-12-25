import sys


# 두값의 차가 음수이면 0을 반환
def remain(num, h):
    if num - h >= 0:
        return num - h
    else:
        return 0


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return mid


n, m = map(int, input().split())
input_data = sys.stdin.readline().rstrip()
n_lst = list(map(int, input_data.split()))
n_lst = sorted(n_lst, reverse=False)
n_lst_max = n_lst[-1]
n_lst_min = n_lst[0]

# range(시작하는 숫자, 끝나는 숫자, 증가분)
# h_list : h 후보 리스트
# m_list : h 로 자른 떡의 나머지부분의 sum 값. 즉, binary_search 함수의 array 로 들어갈 배열
h_list = [i for i in range(n_lst_max, n_lst_min - 1, -1)]
m_list = []

for h in h_list:
    lst = []
    for i in n_lst:
        lst.append(remain(i, h))
    # sum(lst) : h로 잘린 나머지 떡의 길이의 합
    m_list.append(sum(lst))

# m_list에서 target인 m의 index
# == h_list(h값들의 후보리스트)에서 m이 나오게 하는 h(절단기 높이)의 index(위치)
h_list_idx = binary_search(m_list, m, 0, len(m_list) - 1)
print(h_list[h_list_idx])

'''
4 6
19 15 10 17
'''
