def bs_recursion(lst, start, end):
    global target
    if start > end:
        return None
    middle = (start + end) // 2
    if target > lst[middle]:
        return bs_recursion(lst, middle + 1, end)
    elif target < lst[middle]:
        return bs_recursion(lst, start, middle - 1)
    elif target == lst[middle]:
        return middle


target = int(input())
array = list(map(int, input().split()))

result = bs_recursion(array, 0, len(array) - 1)
print(f'array[{result}] = {array[result]}')

'''
12
0 2 4 6 8 10 12 14 16 18
'''