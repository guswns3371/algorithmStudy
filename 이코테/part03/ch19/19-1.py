from collections import deque


def get_distance(shark_loc, fish_loc, p_visited):  # bfs
    kx, ky = shark_loc
    fx, fy = fish_loc

    q = deque([[0, kx, ky]])
    p_visited[kx][ky] = 1

    while q:
        ndist, nx, ny = q.popleft()
        if nx == fx and ny == fy:
            return ndist

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                continue
            if p_visited[xx][yy] == 1:
                continue
            if graph[xx][yy] > shark_size:  # 아기상어 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다
                continue

            p_visited[xx][yy] = 1
            q.append([ndist + 1, xx, yy])

    return -1  # 최단 거리를 구할 수 없는 경우


n = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
shark = []
fishes = []

shark_size = 2
num_fish = 0
num_ate = 0
time = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            shark = [x, y]  # 아기 상어 위치
        elif graph[x][y] != 0:
            fishes.append([x, y])  # 물고기 위치
            num_fish += 1

while fishes:
    neighbor_fish = []

    for fish in fishes:  # 먹을 수 있는 물고기를 찾는다
        fx, fy = fish
        if graph[fx][fy] < shark_size:  # 먹을 수 있는 물고기인 경우
            visited = [[0 for _ in range(n)] for _ in range(n)]
            dist = get_distance(shark, [fx, fy], visited)
            if dist != -1:
                neighbor_fish.append([dist, [fx, fy]])  # 물고기까지 거리, 물고기 위치

    if len(neighbor_fish) == 0:  # 먹을 수 있는 물고기가 없으면 gg
        break

    neighbor_fish.sort()  # 거리 순으로 정렬, x순으로 정렬, y순으로 정렬
    nfdist, nfish = neighbor_fish[0]

    fishes.remove(nfish)
    graph[nfish[0]][nfish[1]] = 0
    graph[shark[0]][shark[1]] = 0
    time += nfdist
    shark = nfish  # 아기상어의 위치를 물고기 위치로 바꾼다
    num_ate += 1

    graph[shark[0]][shark[1]] = 9
    if num_ate == shark_size:
        shark_size += 1
        num_ate = 0

    # print(f"shark={shark}({shark_size}), eat={neighbor_fish[0]}, ate={num_ate}")
    # for x in range(n):
    #     for y in range(n):
    #         print(graph[x][y], end=" ")
    #     print()

print(time)
