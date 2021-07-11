"""
바이러스 https://www.acmicpc.net/problem/2606
bfs 이용
"""
from collections import deque

n = int(input())
m = int(input())
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

q = deque([1])
visited[1] = 1
count = 0
while q:
    now = q.popleft()
    for node in edges[now]:
        if visited[node] == 0:
            visited[node] = 1
            q.append(node)
            count += 1
print(count)
