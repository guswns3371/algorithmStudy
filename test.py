from bisect import bisect_left, bisect_right, bisect

nums = [0, 1, 2, 3, 4, 5]
print(bisect_right(nums, 2))  # 3
print(bisect_left(nums, 2))  # 2
print(bisect(nums, 2))  # 3

nums = [0, 1, 3, 3, 4, 5]
print(bisect_right(nums, 2))  # 2
print(bisect_left(nums, 2))  # 2
print(bisect(nums, 2))  # 2

nums = [0, 1, 2, 2, 4, 5]
print(bisect_right(nums, 2))  # 4
print(bisect_left(nums, 2))  # 2
print(bisect(nums, 2))  # 4
