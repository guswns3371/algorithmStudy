from collections import deque

INF = int(1e9)
n, m, k, x = map(int, input().split())
path = [[] for _ in range(n + 1)]
min_dist = [INF] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)

min_dist[x] = 0
q = deque([[x, 0]])

while q:
    city, dist = q.popleft()

    # x에서 현재 노드까지의 거리가 k인 경우
    if dist == k:
        result.append(city)
        continue

    for next_city in path[city]:
        if next_city != x:
            if dist + 1 < min_dist[next_city]:
                min_dist[next_city] = dist + 1
                q.append([next_city, min_dist[next_city]])

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)

