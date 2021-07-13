"""
영역 구하기 https://www.acmicpc.net/problem/2583
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
result = []

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            graph[x][y] = 1

for y in range(m):
    for x in range(n):
        if visited[x][y] == 1 or graph[x][y] == 1:
            continue
        q = deque([[x, y]])
        visited[x][y] = 1
        count = 0
        while q:
            a, b = q.popleft()
            count += 1
            for i in range(4):
                xx = a + dx[i]
                yy = b + dy[i]
                if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] != 1 and visited[xx][yy] != 1:
                    visited[xx][yy] = 1
                    q.append([xx, yy])
        result.append(count)

result.sort()
print(len(result))
for r in result:
    print(r, end=" ")
