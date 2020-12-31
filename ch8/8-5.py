x = int(input())

dp_table = [0] * (x + 1)

if x >= 2:
    dp_table[2] = 1
if x >= 3:
    dp_table[3] = 1
if x >= 5:
    dp_table[5] = 1

for i in range(2, x + 1):
    dp_table[i] = 1 + dp_table[i - 1]
    if i % 2 == 0:
        dp_table[i] = min(1 + dp_table[i // 2], dp_table[i])
    if i % 3 == 0:
        dp_table[i] = min(1 + dp_table[i // 3], dp_table[i])
    if i % 5 == 0:
        dp_table[i] = min(1 + dp_table[i // 5], dp_table[i])

'''
이것과 차이점이 뭘까?
만약 3의 경우
dp_table[3] = 1 이 if i > 1 구문에 의해 dp_table[3] = 1 + dp_table[2]의 값으로 변경된다
for i in range(2, x + 1):
    dp_table[i] = 1 + dp_table[i - 1]
    if i % 2 == 0:
        dp_table[i] = min(dp_table[2] + dp_table[i // 2], dp_table[i])
    if i % 3 == 0:
        dp_table[i] = min(dp_table[3] + dp_table[i // 3], dp_table[i])
    if i % 5 == 0:
        dp_table[i] = min(dp_table[5] + dp_table[i // 5], dp_table[i])
'''

result = dp_table[x]
print(dp_table, result)
