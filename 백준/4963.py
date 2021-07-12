"""
섬의 개수 https://www.acmicpc.net/problem/4963
"""
from collections import deque

dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]
result = []
while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    count = 0
    graph = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 0 or visited[x][y] == 1:
                continue
            q = deque([[x, y]])
            visited[x][y] = 1
            count += 1
            while q:
                a, b = q.popleft()
                for i in range(8):
                    xx = a + dx[i]
                    yy = b + dy[i]

                    if not (0 <= xx < h and 0 <= yy < w):
                        continue
                    if graph[xx][yy] == 0 or visited[xx][yy] == 1:
                        continue
                    visited[xx][yy] = 1
                    q.append([xx, yy])
    result.append(count)
for r in result:
    print(r)
