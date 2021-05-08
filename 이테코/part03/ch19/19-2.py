def gprint(p_graph, p_dir_graph):
    for px in range(4):
        for py in range(4):
            if [px, py] == shark:
                print(f"상{dd[p_dir_graph[px][py] - 1]}", end=" ")
            else:
                print(f"{p_graph[px][py]}{dd[p_dir_graph[px][py] - 1]}", end=" ")
        print()
    print("-----------------")


def eat_fish(p_fish):
    # list를 원소로 가지는 list는 remove()로 원소를 삭제할 수 없다.
    eat = graph[shark[0]][shark[1]]  # 물고기 먹음
    graph[p_fish[0]][p_fish[1]] = 0  # 물고기를 그래프에서 지움
    return [f for f in fishes if [f[1], f[2]] != p_fish], eat


def change_fish(ox, oy, cx, cy):
    r_fish = []
    for i in range(len(fishes)):
        fnum, fx, fy = fishes[i]
        if [fx, fy] == [ox, oy]:
            r_fish.append([fnum, cx, cy])
        elif [fx, fy] == [cx, cy]:
            r_fish.append([fnum, ox, oy])
        else:
            r_fish.append(fishes[i])
    return r_fish


def moving_fish():
    global fishes
    for i in range(len(fishes)):
        fnum, fx, fy = fishes[i]
        fdirect = direct_graph[fx][fy]

        # print("물고기 대이동 중")
        # print(f"fish={fnum}{dd[(fdirect % 8) - 1]} ({fx},{fy})={graph[fx][fy]}")

        for _ in range(8):
            xx = fx + dx[(fdirect % 8) - 1]
            yy = fy + dy[(fdirect % 8) - 1]

            if xx < 0 or yy < 0 or xx >= 4 or yy >= 4:
                fdirect += 1
                continue
            if [xx, yy] == shark:
                fdirect += 1
                continue

            # 두 물고기의 위치를 바꾼다.
            # print(f"물고기 바꾸기 : {graph[fx][fy]}{dd[direct_graph[fx][fy] - 1]} >> {graph[xx][yy]}{dd[direct_graph[xx][yy] - 1]}")

            graph[fx][fy], graph[xx][yy] = graph[xx][yy], graph[fx][fy]
            direct_graph[fx][fy], direct_graph[xx][yy] = direct_graph[xx][yy], fdirect % 8
            fishes = change_fish(fx, fy, xx, yy)
            break

        # gprint(graph, direct_graph)


def eating_fish():
    global shark, fishes
    # 먹을 수 있는 후보 물고기 리스트
    nominee_fish = []
    kx, ky = shark
    kdirect = direct_graph[kx][ky]

    for _ in range(4):
        nx = kx + dx[kdirect - 1]
        ny = ky + dy[kdirect - 1]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            break
        if graph[nx][ny] == 0:
            kx = nx
            ky = ny
            continue

        nominee_fish.append([graph[nx][ny], nx, ny])
        kx = nx
        ky = ny

    if len(nominee_fish) == 0:
        return None
    elif len(nominee_fish) == 1:
        num, x, y = nominee_fish[0]
        shark = [x, y]
        fishes, ate = eat_fish(shark)
        print("상어 이동")
        print(f"먹어치울 고기들={nominee_fish}")
        print(f"꿀꺽={num}{dd[direct_graph[x][y] - 1]}")
        gprint(graph, direct_graph)
        print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
        print()
        return ate
    else:
        nominee_fish.sort()
        nominee_fish.reverse()

        for nom in nominee_fish:
            num, x, y = nom
            ndirect = direct_graph[x][y]
            nx = x + dx[ndirect - 1]
            ny = y + dy[ndirect - 1]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            shark = [x, y]
            fishes, ate = eat_fish(shark)

            print("상어 이동")
            print(f"먹어치울 고기들={nominee_fish}")
            print(f"꿀꺽={num}{dd[direct_graph[x][y] - 1]}")
            gprint(graph, direct_graph)
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            print()
            return ate


data = []
graph = []
direct_graph = []
fishes = []
ate_fish = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dd = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗ "]

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
fishes, ate = eat_fish(shark)  # 0,0의 물고기 먹음
ate_fish += ate

while True:
    moving_fish()

    print("물고기 대이동 후")
    gprint(graph, direct_graph)

    a = eating_fish()
    if a is not None:
        ate_fish += a
    else:
        break

print(ate_fish)