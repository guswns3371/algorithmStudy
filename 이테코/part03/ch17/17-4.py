from collections import deque

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 통로 , 모든 통로의 가중치를 1로 둔다
    graph[a].append(b)
    graph[b].append(a)

dist[1] = 0
q = deque([[dist[1], 1]])

for g in graph:
    print(g)

print()

while q:
    cost, now = q.popleft()

    for node in graph[now]:

        if dist[node] <= dist[now] + 1 and dist[node] != INF:
            continue
        dist[node] = min(dist[node], dist[now] + 1)
        q.append([dist[node], node])

dist[0] = -1
print(dist)

barn_dist = max(dist)
barn_num = dist.index(barn_dist)
barn_count = dist.count(barn_dist)

print(barn_num, barn_dist, barn_count)
"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
