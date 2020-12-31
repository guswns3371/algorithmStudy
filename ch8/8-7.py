n = int(input())

dp_table = [0] * (n + 1)

dp_table[1] = 1
dp_table[2] = 3

'''
dp_table[i] =
  dp_table[i-1] + dp_table[1]
  dp_table[i-2] + dp_table[2]
  ...
  dp_table[2] + dp_table[i-2]
  dp_table[1] + dp_table[i-1]
  -i
  
(예시)
dp_table[3] =
  dp_table[2] + dp_table[1]
  dp_table[1] + dp_table[2]
  -3
  '''
# 나의 답안
# 일반화가 제대로 안된 점화식
for i in range(3, n + 1):
    for j in range(i):
        dp_table[i] += dp_table[i - j] + dp_table[j]
    dp_table[i] -= i

result = dp_table[n] % 796796
print('<1>', dp_table, result)

# 모범답안
# 점화식은 생각보다 간단하다
dp_table = [0] * (n + 1)

dp_table[1] = 1
dp_table[2] = 3
for i in range(3, n + 1):
    dp_table[i] = (dp_table[i - 1] + 2 * dp_table[i - 2])

result = dp_table[n] % 796796
print('<2>', dp_table, result)
