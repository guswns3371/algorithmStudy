def gprint(p_graph):
    for px in range(4):
        for py in range(4):
            print(p_graph[px][py], end=" ")
        print()
    print("-----------------")


def eat_fish(p_fish):  # list를 원소로 가지는 list는 remove()로 원소를 삭제할 수 없다.
    global ate_fish
    ate_fish += graph[shark[0]][shark[1]]  # 물고기 먹음
    graph[p_fish[0]][p_fish[1]] = 0  # 물고기를 그래프에서 지움
    return [f for f in fishes if [f[1], f[2]] != p_fish]


data = []
graph = []
direct_graph = []
fishes = []
ate_fish = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for _ in range(4):
    data.append(list(map(int, input().split())))

for x in range(4):
    gtemp = []
    dtemp = []
    for y in range(4):
        gtemp.append(data[x][2 * y])
        dtemp.append(data[x][2 * y + 1])
        fishes.append([data[x][2 * y], x, y])  # [물고기 번호, x, y]

    graph.append(gtemp)
    direct_graph.append(dtemp)

fishes.sort()  # 물고기 번호 기준으로 정렬

shark = [0, 0]  # 0,0 위치로 이동
fishes = eat_fish(shark)  # 0,0의 물고기 먹음

while True:
    for fish in fishes:
        fnum, fx, fy = fish
        fdirect = direct_graph[fx][fy]
        for i in range(8):
            xx = fx + dx[(fdirect + i - 1) % 8]
            yy = fy + dy[(fdirect + i - 1) % 8]

            if xx < 0 or yy < 0 or xx >= 4 or yy >= 4:
                continue
            if [xx, yy] == shark:
                continue

            fdir = (fdirect + i - 1) % 8 + 1

            # 두 물고기의 위치를 바꾼다.
            graph[fx][fy] = graph[xx][yy]
            graph[xx][yy] = fnum
            direct_graph[fx][fy] = direct_graph[xx][yy]
            direct_graph[xx][yy] = fdir

            break

    nominee_fish = []
    kx, ky = shark
    kdirect = direct_graph[kx][ky]

    while True:
        nx = kx + dx[kdirect - 1]
        ny = ky + dy[kdirect - 1]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        if graph[nx][ny] == 0:
            continue

        nominee_fish.append([graph[nx][ny], nx, ny])

    if len(nominee_fish) == 0:
        break

    nominee_fish.sort()
    num, x, y = nominee_fish[0]
    shark = [x, y]
    fishes = eat_fish(shark)

print(ate_fish)
