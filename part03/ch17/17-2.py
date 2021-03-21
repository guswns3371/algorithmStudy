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
                visited[node] = 1

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

5 10
4 2 
3 5 
2 5 
1 3 
2 1 
1 5 
3 4 
3 2 
1 4 

4 6
4 1 
3 4 
1 3 
2 4 
2 1 

6 7
6 1 
1 3 
1 4 
4 6 
2 1 
4 5 

9 15
5 2 
9 6 
4 9 
1 5 
5 8 
5 7 
3 7 
2 3 
1 3 
8 1 
2 8 
6 1 
5 9 
9 8 

7 13
1 2 
1 5 
3 7 
2 3 
3 5 
7 2 
1 7 
4 5 
6 2 
5 6 
4 7 
6 7

9 17
8 5 
2 1 
3 5 
7 6 
7 2 
5 6 
3 6 
6 1 
7 4 
5 1 
8 6 
6 2 
9 5 
4 1 
7 8 
9 7 
"""
