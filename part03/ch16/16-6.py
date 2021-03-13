a = list(input())
b = list(input())

a_len = len(a)
b_len = len(b)

dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]
dp[0][0] = 0

for i in range(a_len + 1):
    dp[i][0] = i

for i in range(b_len + 1):
    dp[0][i] = i

for y in range(a_len + 1):
    for x in range(b_len + 1):
        print(dp[y][x], end=" ")
    print()

for y in range(1, a_len + 1):
    for x in range(1, b_len + 1):
        if a[y - 1] == b[x - 1]:
            dp[y][x] = dp[y - 1][x - 1]
        else:
            dp[y][x] = min(dp[y - 1][x] + 1, dp[y][x - 1] + 1, dp[y - 1][x - 1] + 1)

for y in range(a_len + 1):
    for x in range(b_len + 1):
        print(dp[y][x], end=" ")
    print()

print(dp[a_len][b_len])

"""
MICROSOFT
NCSOFT
"""
