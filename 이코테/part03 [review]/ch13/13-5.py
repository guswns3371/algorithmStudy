from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operator = []
for idx, val in enumerate(list(map(int, input().split()))):
    operator += [idx] * val

cases = list(set(permutations(operator, len(nums) - 1)))

min_result = int(1e9)
max_result = -int(1e9)
for case in cases:
    result = nums[0]
    for i in range(1, len(nums)):
        if case[i - 1] == 0:
            result += nums[i]
        elif case[i - 1] == 1:
            result -= nums[i]
        elif case[i - 1] == 2:
            result *= nums[i]
        elif case[i - 1] == 3:
            if result > 0:
                result = result // nums[i]
            else:
                result = -(abs(result) // nums[i])
    if result < min_result:
        min_result = result
    if result > max_result:
        max_result = result

print(max_result)
print(min_result)
"""
7
3 4 5 1 2 6 8
1 2 3 0
"""
