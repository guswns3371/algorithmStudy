# [퇴사](https://www.acmicpc.net/problem/14501)
"""
특정 일 이후 가장 최적의 스케쥴은 정해져 있다.
예를 들면, 3일차 이후 최대 수익을 구하는 스케쥴은 3일차, 4일차 스케쥴을 선택하는 것 뿐이다.
"""
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [-1] * (n + 1)
dp[n] = 0
for day in reversed(range(n)):
    term, value = data[day]
    if day + term > n:
        dp[day] = max(0, max(dp[day:]))
        continue
    dp[day] = max(max(dp[day:]), value + dp[day + term])

print(max(dp))
