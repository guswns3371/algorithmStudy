import sys

n, m = map(int, input().split())
input_data = sys.stdin.readline().rstrip()
n_lst = list(map(int, input_data.split()))


# 두 값 num,h의 차가 음수이면 0을 반환
def remain(num, h):
    if num - h >= 0:
        return num - h
    else:
        return 0


def binary_new(array, target, start, end):
    if start > end:
        return None

    # mid는 곧 h(절단기의 높이) 를 의미
    mid = (start + end) // 2

    # array[mid] 대신 sum_remain_n_lst 을 target과 비교해야한다.
    sum_remain_n_lst = 0
    for i in array:
        sum_remain_n_lst += remain(i, mid)

    if target > sum_remain_n_lst:
        # 일반적 이진 탐색과 다르게 mid가 start에 가까워질수록 => sum_remain_n_lst값이 커짐
        # target이 더 크면, start = mid +1 가 아닌 => end = mid -1
        return binary_new(array, target, start, mid - 1)
    elif target < sum_remain_n_lst:
        # target이 작으면, end = mid -1 이 아닌 => start = mid +1
        return binary_new(array, target, mid + 1, end)
    else:
        return mid


result = binary_new(n_lst, m, 0, max(n_lst))
print(result)

'''
4 6
19 15 10 17
'''
