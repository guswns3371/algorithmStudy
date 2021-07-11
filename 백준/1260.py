# DFS와 BFS https://www.acmicpc.net/problem/1260
from collections import deque


# stack -> 재귀는 stack
def dfs(start, dfs_list):
    dfs_list.append(str(start))

    for node in edges[start]:
        if str(node) not in dfs_list:
            dfs(node, dfs_list)


# queue
def bfs(start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        bfs_list.append(str(now))
        for node in edges[now]:
            if visited[node] == 0:
                visited[node] = 1
                q.append(node)


n, m, v = map(int, input().split())
edges = [[] for _ in range(n + 1)]
dfs_list = []
bfs_list = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for edge in edges:
    edge.sort()

dfs(v, dfs_list)
bfs(v)

print(" ".join(dfs_list))
print(" ".join(bfs_list))
