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

5
1 3 1 5 1 9
o x x x x o
o x x x o x
o x x o x x
등등은
최댓값을 구할 수 없는 방식

0 1 2 3 4 5
o x o x o x
x o x o x o
최댓값을 구해야하므로 무조건 한칸만 건너 뛰어야 한다
결국 2가지만 존재
'''
