target = int(input())
array = list(map(int, input().split()))


def bs_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        elif target == array[mid]:
            return mid

    return None


result = bs_loop(array, target, 0, len(array) - 1)
print(result + 1)
 
'''
12
0 2 4 6 8 10 12 14 16 18
'''
