from collections import deque


def bfs_spread_virus(graph, start, visited):
    x, y = start
    queue = deque([[x, y]])

    while queue:
        nx, ny = queue.pop()
        print(nx, ny, "pop")
        for d in range(5):
            xx = nx + dx[d]
            yy = ny + dy[d]
            print(xx, yy, end=" : ")
            # 지도를 벗어나는 경우, 방문했던 경우는 건너 뛴다.
            if xx < 0 or yy < 0 or xx >= n or yy >= m:
                print("불가능")
                continue
            if graph[xx][yy] == 1:
                print("벽")
                continue
            if visited[xx][yy] == 1:
                print("이미방문")
                continue
            # 빈칸일 경우만 바이러스 퍼뜨리기
            if graph[xx][yy] == 0:
                graph[xx][yy] = 2
                print("감염", end=",")

            if visited[xx][yy] == 0:
                queue.append([xx, yy])
                print("방문!")
                visited[xx][yy] = 1
                for a in range(n):
                    for b in range(m):
                        print(visited[a][b], end=" ")
                    print()
                print()
            # for a in range(n):
            #     for b in range(m):
            #         print(graph[a][b], end=" ")
            #     print()
            # print()
            # print()


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
infected = []
visited = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    graph[i] = (list(map(int, input().split())))
    # 바이러스가 감연된 위치를 infected 리스트에 넣는다
    for j in range(m):
        if graph[i][j] == 2:
            infected.append([i, j])

for virus in infected:
    print(virus)
    bfs_spread_virus(graph, virus, visited)

print("결과")
# total : 안전 영역 크기
total = 0
for a in range(n):
    for b in range(m):
        print(graph[a][b], end=" ")
        if graph[a][b] == 0:
            total += 1
    print()

print(total)
