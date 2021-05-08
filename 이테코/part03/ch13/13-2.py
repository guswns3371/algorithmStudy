from collections import deque
import itertools
import copy


def spread_virus_bfs(v_graph, start, visited):
    x, y = start
    queue = deque([[x, y]])
    visited[x][y] = 1

    while queue:
        nx, ny = queue.popleft()
        for d in range(4):
            xx = nx + dx[d]
            yy = ny + dy[d]
            # 지도를 벗어나는 경우, 방문했던 경우는 건너 뛴다.
            if xx < 0 or yy < 0 or xx >= n or yy >= m:
                continue
            if v_graph[xx][yy] == 1:
                continue
            if visited[xx][yy] == 1:
                continue
            # 빈칸일 경우만 바이러스 퍼뜨리기
            if v_graph[xx][yy] == 0:
                v_graph[xx][yy] = 2

            queue.append([xx, yy])
            visited[xx][yy] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
infected = []
wall_list = []
for i in range(n):
    graph[i] = (list(map(int, input().split())))
    # 바이러스가 감연된 위치를 infected 리스트에 넣는다
    for j in range(m):
        if graph[i][j] == 2:
            infected.append([i, j])
        elif graph[i][j] == 0:
            wall_list.append([i, j])

# 벽 3개를 세우는 경우의 수
brute_case = [list(t) for t in itertools.combinations([i for i in range(len(wall_list))], 3)]

max_size = -int(1e9)
for case in brute_case:
    c_graph = copy.deepcopy(graph)
    virus_visited = [[0 for _ in range(m)] for _ in range(n)]
    for c in case:
        print(f"({wall_list[c][0]},{wall_list[c][1]})", end=" ")
        # 벽을 세운다
        c_graph[wall_list[c][0]][wall_list[c][1]] = 1
    print("벽 설치")
    # 바이러스 퍼뜨리기
    for virus in infected:
        spread_virus_bfs(c_graph, virus, virus_visited)

    # total : 안전 영역 크기
    total = 0
    for a in range(n):
        for b in range(m):
            print(c_graph[a][b], end=" ")
            if c_graph[a][b] == 0:
                total += 1
        print()
    if max_size < total:
        max_size = total
    print("total", total, ", ", "max_size", max_size)

print(max_size)
