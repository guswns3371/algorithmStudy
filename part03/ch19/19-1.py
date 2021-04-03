from collections import deque

n = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# visited = [[0 for _ in range(n)] for _ in range(n)]
graph = []
shark = []
fishes = 0  # 물고기 개수
ate_fishes = 0  # 먹은 물고기 개수
time = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            shark = [2, 0, x, y]  # 아기 상어 크기, 지난 칸의 개수,위치
        elif graph[x][y] != 0:
            fishes += 1  # 물고기 크기, 위치


def bfs(p_shark):
    global time, ate_fishes, fishes
    q = deque(p_shark)

    while q:
        ksize, kcell, kx, ky = q.popleft()
        neigbor_fish = []  # 먹을 수 있는 주변 물고기 리스트

        for i in range(4):
            xx = kx + dx[i]
            yy = ky + dy[i]

            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                continue

            fsize = graph[xx][yy]
            if fsize > 0 and fsize != 9:  # 물고기가 있는 위치라면
                if fsize <= ksize:  # 아기상어의 크기보다 작거나 같은 물고기를 neigbor_fish에 담는다.
                    neigbor_fish.append([fsize, xx, yy])

        if fishes - ate_fishes <= 0:
            break  # 엄마 상어에게 도움 요청

        elif len(neigbor_fish) == 1:
            nsize, nx, ny = neigbor_fish.pop(0)
            graph[nx][ny] = 0  # 물고기를 먹어 치운다.
            ate_fishes += 1  # 먹은 물고기 수
            if ate_fishes == ksize:  # 아기 상어의 크기와 물고기의 크기가 같은 경우
                ksize += 1

            q.append([ksize, kcell + 1, nx, ny])  # 지나친 칸의 개수에 +1

        elif len(neigbor_fish) > 1:
            closest_fish = []  # 거리가 가까운 물고기 리스트
            for fish in neigbor_fish:
                pass

        time += 1
