n = int(input())

time_price = []
dp = []
for _ in range(n):
    t_list = list(map(int, input().split()))
    time_price.append(t_list)
    dp.append(t_list)

for i in reversed(range(n)):
    nt, np = dp[i]
    if i + nt > n:
        dp[i][1] = -1

print("dp initial")
for i in range(n):
    print(f"day={i} ", dp[i][0], dp[i][1])
print()

print("===========")
for day in reversed(range(n)):
    time, price = dp[day]

    if day + time >= n:  # 현재 날짜와 걸리는 시간을 합쳤을 때, 퇴사일 보다 초과할 경우
        continue

    max_price = -int(1e9)
    for i in range(day + time, n):
        if dp[i][1] != -1 and max_price < dp[i][1]:
            max_price = dp[i][1]

    if max_price > 0:
        dp[day][1] += max_price

print("dp result")
for i in range(n):
    print(f"day={i} ", dp[i][0], dp[i][1])
print()

max_time = -int(1e9)

for i in range(n):
    if max_time < dp[i][1]:
        max_time = dp[i][1]

if max_time > 0:
    print(max_time)
else:
    print(0)
