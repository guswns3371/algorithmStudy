from collections import deque

n, L, R = map(int, input().split())
graph = []
count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    graph.append(list(map(int, input().split())))

while True:
    # 인구 이동마다 연합이 새로 만들어진다
    unions = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 자기 자신으로 이뤄진 연합
            q = []
            tunion = deque([[x, y]])
            while tunion:
                nx, ny = tunion.popleft()
                # 주변 나라를 확인하여 연합을 키운다
                for i in range(4):
                    xx = nx + dx[i]
                    yy = ny + dy[i]

                    if xx < 0 or yy < 0 or xx >= n or yy >= n:
                        continue
                    if visited[xx][yy] == 1:
                        continue
                    if L <= abs(graph[xx][yy] - graph[nx][ny]) <= R:
                        tunion.append([xx, yy])
                        q.append([xx, yy])
                        visited[xx][yy] = 1

            if len(q) > 1:
                unions.append(q)

    check = True
    for union in unions:
        check = False
        # 연합속 총 인구
        every = 0
        for u in union:
            every += graph[u[0]][u[1]]
        # 인구이동
        for u in union:
            graph[u[0]][u[1]] = every // len(union)
    if check:
        break
    count += 1

print(count)
