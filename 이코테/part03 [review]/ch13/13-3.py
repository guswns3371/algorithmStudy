from collections import deque
import copy


def gprint(data):
    for dd in data:
        for d in dd:
            print(d, end=" ")
        print()
    print()


n, k = map(int, input().split())
graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
q = [deque([]) for _ in range(k + 1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

# (바이러스, x위치, y위치) -> 우선순위 큐
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q[graph[i][j]].append([i, j])
            visited[i][j] = 1

time = 0
while time != s:
    for v in range(k):
        tq = deque([])
        while q[v + 1]:
            vnum = v + 1
            vx, vy = q[v + 1].popleft()

            for i in range(4):
                xx = vx + dx[i]
                yy = vy + dy[i]

                # 다른 바이러스가 존재하거나, 맵을 벗어난 경우
                if xx < 0 or yy < 0 or xx >= n or yy >= n:
                    continue
                if graph[xx][yy] != 0:
                    continue
                graph[xx][yy] = vnum
                visited[xx][yy] = 1
                tq.append([xx, yy])

        q[v + 1] = copy.deepcopy(tq)

    time += 1

    count = 0
    for visit in visited:
        count += sum(visit)
    if count == n*n:
        break

if graph[x - 1][y - 1] == 0:
    print(0)
else:
    print(graph[x - 1][y - 1])

"""
5 3
1 0 2 0 0
0 0 0 0 0
3 0 0 3 0
0 1 0 0 3
2 0 0 0 0
10 3 2
"""
