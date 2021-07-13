# [병사 배치하기](https://www.acmicpc.net/problem/18353)
n = int(input())
data = list(map(int, input().split()))
dp = []
for i in range(n):
    print("{:<2}".format(i + 1), end=" ")
print()
for i in range(n):
    print("{:<2}".format(data[i]), end=" ")
print()