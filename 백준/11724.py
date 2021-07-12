"""
연결 요소의 개수 https://www.acmicpc.net/problem/11724
연결 요소란 : https://velog.io/@kjh107704/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C
"""
from collections import deque

n, m = map(int, input().split())
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
count = 0
for _ in range(m):
    u, v = list(map(int, input().split()))
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, n + 1):
    if visited[i] == 1:
        continue

    count += 1
    q = deque([i])
    visited[i] = 1
    while q:
        now = q.popleft()
        for node in edges[now]:
            if visited[node] == 0:
                visited[node] = 1
                q.append(node)
print(count)
