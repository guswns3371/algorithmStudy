import random

n, m = random.randrange(1, 21), random.randrange(1, 101)
dp_table = [10001] * (m + 1)
n_list = []

for i in range(n):
    num = random.randrange(1, 101)
    while n_list.__contains__(num):
        num = random.randrange(1, 101)
        break
    n_list.append(num)
array = n_list

print(n, m)
print(n_list)


































# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print('<2>', -1)
else:
    print('<2>', d[m])
