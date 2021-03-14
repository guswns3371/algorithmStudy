from collections import deque


def find_chart(start):
    visited = [0] * (n + 1)
    dist = [INF] * (n + 1)
    q = deque([[0, start]])

    dist[start] = 0
    visited[start] = 1

    while q:
        cost, now = q.popleft()

        for node in graph[now]:
            if visited[node] != 1:
                dist[node] = min(dist[node], dist[now] + 1)
                q.append([dist[node], node])

    dist[0] = -1
    print(dist)
    for ii in range(1, n + 1):
        if ii == start:
            continue

        if dist[ii] != INF:
            biggers[start].append(ii)
        else:
            others[start].append(ii)


INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
biggers = [[] for _ in range(n + 1)]
others = [[] for _ in range(n + 1)]
know = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(n):
    print(f"{i + 1}번 학생 시작")
    find_chart(i + 1)

print("bigger")
for i in range(n):
    student = i + 1
    print(f"{student}번 학생 보다 큰 놈들 : {biggers[student]}")
    print(f"그 이외의 놈들 : {others[student]}")
    dunno = len(others[student])
    for other in others[student]:
        if student in biggers[other]:
            dunno -= 1

    if dunno == 0:
        know += 1
        print(f"{student} 학생 순위 정확히 앎 🔥")
    else:
        print(f"{student} 학생 순위 모름, 확실치 않은 핵생수={dunno}")

print(know)
"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
