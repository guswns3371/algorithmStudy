import copy

dx = [-1, 0, 1]
dy = [1, 1, 1]
answer = []

# t = int(input())

# for _ in range(t):
n, m = map(int, input().split())
lst = list(map(int, input().split()))

graph = []
result = []

for i in range(n):
    graph.append(lst[m * i:m * i + m])

d = copy.deepcopy(graph)

for y in reversed(range(m - 1)):
    for x in range(n):
        max_num = -int(1e9)
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if max_num < d[nx][ny]:
                max_num = d[nx][ny]

        d[x][y] += max_num


result = -int(1e9)
for i in range(n):
    if result < d[i][0]:
        result = d[i][0]
print(result)
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
