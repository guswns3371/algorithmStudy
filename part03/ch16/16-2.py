import copy

n = int(input())
graph = []
dx = [1, 1]
dy = [0, 1]

for i in range(n):
    lst = list(map(int, input().split()))

    for _ in range(n - i - 1):
        lst.append(-1)  # 빈 부분은 모두 -1으로 채운다
    graph.append(lst)

dp = copy.deepcopy(graph)

print("graph")
for g in graph:
    for gg in g:
        print(gg, end=" ")
    print()

for x in reversed(range(n - 1)):
    for y in range(n):

        if dp[x][y] == -1:
            continue

        max_path = -int(1e9)

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if max_path < dp[nx][ny]:
                max_path = dp[nx][ny]

        dp[x][y] += max_path

print("dp table")
for g in dp:
    for gg in g:
        print(gg, end=" ")
    print()

print(dp[0][0])
