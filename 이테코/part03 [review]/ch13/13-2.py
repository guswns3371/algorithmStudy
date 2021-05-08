from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = []
viruses = []
wall = []
blank = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            viruses.append([x, y])
        elif graph[x][y] == 1:
            wall.append([x, y])
        elif graph[x][y] == 0:
            blank.append([x, y])

result = []
cases = list(combinations(blank, 3))

for case in cases:
    # 벽 3개를 설치할 하나의 케이스

    # 그래프 새로 copy
    v_graph = deepcopy(graph)

    # 벽 3개 설치
    for c_one in case:
        v_graph[c_one[0]][c_one[1]] = 1

    # 각 바이러스에서 bfs 실시
    for virus in viruses:
        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque([virus])
        visited[virus[0]][virus[1]] = 1

        while q:
            vx, vy = q.popleft()

            for i in range(4):
                xx = vx + dx[i]
                yy = vy + dy[i]

                # 그래프 범위를 벗어나거나, 이미 방문한 적이 있는 곳인 경우
                if xx < 0 or yy < 0 or xx >= n or yy >= m or visited[xx][yy] == 1:
                    continue

                # 움직인 곳이 원래 벽인 경우, 새롭게 설치한 벽인 경우
                if v_graph[xx][yy] != 0:
                    continue

                q.append([xx, yy])
                visited[xx][yy] = 1
                v_graph[xx][yy] = 2

    safe_count = 0
    for v_row in v_graph:
        safe_count += v_row.count(0)
    result.append(safe_count)

print(max(result))
