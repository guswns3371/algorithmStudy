"""
단지번호붙이기 https://www.acmicpc.net/problem/2667
bfs, 완전 탐색 활용
"""
from collections import deque

n = int(input())
result = []
visited = [[0 for _ in range(n)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for x in range(n):
    for y in range(n):
        if graph[x][y] == 0 or visited[x][y] == 1:
            continue

        q = deque([[x, y]])
        visited[x][y] = 1
        count = 1
        while q:
            kx, ky = q.popleft()
            for k in range(4):
                xx = kx + dx[k]
                yy = ky + dy[k]

                if 0 <= xx < n and 0 <= yy < n:
                    if visited[xx][yy] == 0 and graph[xx][yy] != 0:
                        visited[xx][yy] = 1
                        q.append([xx, yy])
                        count += 1
        result.append(count)
result.sort()
print(len(result))
for r in result:
    print(r)
