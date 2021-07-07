# 국영수(https://www.acmicpc.net/problem/10825)
n = int(input())
data = []
for i in range(n):
    data.append(input().split())
data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])
