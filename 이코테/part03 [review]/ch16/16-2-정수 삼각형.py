# [정수 삼각형](https://www.acmicpc.net/problem/1932)
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0 for _ in range(i+1)] for i in range(n)]
dp[0][0] = data[0][0]

for i in range(n - 1):
    for j in range(len(data[i])):
        for k in range(2):
            dp[i + 1][j + k] = max(dp[i + 1][j + k], data[i + 1][j + k] + dp[i][j])

print(max(dp[n-1]))