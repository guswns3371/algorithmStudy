"""
유기농 배추 https://www.acmicpc.net/problem/1012
bfs
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
for t in range(int(input())):
    m, n, k = map(int, input().split())
    baechu = []
    count = 0
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 0 or visited[a][b] == 1:
                continue
            count += 1
            visited[a][b] = 1
            q = deque([[a, b]])
            while q:
                x, y = q.popleft()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]

                    if 0 <= yy < n and 0 <= xx < m:
                        if graph[xx][yy] == 0 or visited[xx][yy] == 1:
                            continue

                        visited[xx][yy] = 1
                        q.append([xx, yy])
    result.append(count)

for r in result:
    print(r)
