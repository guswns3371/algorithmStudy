"""
안전 영역 https://www.acmicpc.net/problem/2468
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
graph = []
max_num = -int(1e9)

for _ in range(n):
    graph.append(list(map(int, input().split())))

# rain == 0 즉, 비가 안내리는 경우도 체크해야 하네?
for rain in range(101):
    count = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 물에 잠기기
    for x in range(n):
        for y in range(n):
            if graph[x][y] <= rain:
                visited[x][y] = -1

    for x in range(n):
        for y in range(n):
            # -1 : 물에 잠긴 부분
            # 1 : 방문한 부분
            if visited[x][y] != 0:
                continue

            visited[x][y] = 1
            q = deque([[x, y]])
            count += 1
            while q:
                a, b = q.popleft()
                for i in range(4):
                    xx = a + dx[i]
                    yy = b + dy[i]

                    if not (0 <= xx < n and 0 <= yy < n):
                        continue
                    if visited[xx][yy] != 0:
                        continue
                    visited[xx][yy] = 1
                    q.append([xx, yy])

    if max_num < count:
        max_num = count
    if count == 0:
        break

print(max_num)
