n = int(input())
food_garage = list(map(int, input().split()))

dp_table = [0] * (n + 1)

dp_table[1] = food_garage[0]
dp_table[2] = max(food_garage[0], food_garage[1])

for i in range(3, n + 1):
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + food_garage[i - 1])

result = max(dp_table)
print(dp_table, result)
'''
4
1 3 1 5
# [0, 1, 3, 3, 8] 8

9
1 2 8 6 1 5 3 7 6
# [0, 1, 2, 9, 9, 10, 14, 14, 21, 21] 21
'''
