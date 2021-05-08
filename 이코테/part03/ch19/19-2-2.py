from copy import deepcopy


def gprint(pshark_location, pgraph, pdgraph):
    for px in range(4):
        for py in range(4):
            if [px, py] == pshark_location:
                print(f"상{dd[pdgraph[px][py] - 1]}", end=" ")
            else:
                print(f"{pgraph[px][py]}{dd[pdgraph[px][py] - 1]}", end=" ")
        print()
    print("-----------------")


def update_fishes(pfishes, px, py):
    return [f for f in pfishes if [f[1], f[2]] != [px, py]]


def eat_fish(pshark_location, pgraph, pfishes):
    kx, ky = pshark_location
    rfish_num = pgraph[kx][ky]

    pgraph[kx][ky] = 0  # kx,ky를 비우고
    pfishes = update_fishes(pfishes, kx, ky)  # fishes리스트에서 kx,ky를 삭제
    return rfish_num, pfishes, pgraph  # 먹은 물고기 번호, fishes 리스트, pgraph


def moving_fish(pshark_location, pgraph, pdgraph, pfishes):
    for i in range(len(pfishes)):
        fnum, fx, fy = pfishes[i]
        fdirect = pdgraph[fx][fy]

        print("!! 물고기 대이동 진행상황")
        print(f"!! fish={fnum}{dd[(fdirect % 8) - 1]} ({fx},{fy})={pgraph[fx][fy]}")

        for _ in range(8):
            xx = fx + dx[(fdirect % 8) - 1]
            yy = fy + dy[(fdirect % 8) - 1]

            if xx < 0 or yy < 0 or xx >= 4 or yy >= 4:
                fdirect += 1
                continue
            if [xx, yy] == pshark_location:
                fdirect += 1
                continue

            # 두 물고기의 위치를 바꾼다.
            print(
                f"!! 물고기 바꾸기 : {pgraph[fx][fy]}{dd[pdgraph[fx][fy] - 1]} >> {pgraph[xx][yy]}{dd[pdgraph[xx][yy] - 1]}")

            pgraph[fx][fy], pgraph[xx][yy] = pgraph[xx][yy], pgraph[fx][fy]
            pdgraph[fx][fy], pdgraph[xx][yy] = pdgraph[xx][yy], fdirect % 8

            # rfishes에서도 [fx,fy] <-> [xx,yy] 위치를 바꿈
            tfishes = []
            for j in range(len(pfishes)):
                tfnum, tfx, tfy = pfishes[j]

                if [tfx, tfy] == [fx, fy]:
                    tfishes.append([tfnum, xx, yy])
                elif [tfx, tfy] == [xx, yy]:
                    tfishes.append([tfnum, fx, fy])
                else:
                    tfishes.append([tfnum, tfx, tfy])

            pfishes = tfishes
            break

        print("!! 바꾼 결과")
        gprint(pshark_location, pgraph, pdgraph)

    return pgraph, pdgraph, pfishes


def get_nominee_fish(shark_location, pgraph, pdgraph):
    rnominee_fish = []
    kx, ky = shark_location
    kdirect = pdgraph[kx][ky]

    for _ in range(4):
        nx = kx + dx[kdirect - 1]
        ny = ky + dy[kdirect - 1]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            break
        if pgraph[nx][ny] == 0:
            kx = nx
            ky = ny
            continue

        rnominee_fish.append([pgraph[nx][ny], nx, ny])
        kx = nx
        ky = ny
    return rnominee_fish


def cycle(i, pnominee, peat_num, pgraph, pdgraph, pfishes):
    rgraph = deepcopy(pgraph)
    rdgraph = deepcopy(pdgraph)
    rfishes = deepcopy(pfishes)

    # 상어 이동
    _, ex, ey = pnominee[i]
    pshark_location = [ex, ey]

    # 물고기 먹음
    fish_num, rfishes, rgraph = eat_fish(pshark_location, rgraph, rfishes)

    # 출력
    print(f"<1> {fish_num}물고기 먹음 ({peat_num}+{fish_num}={peat_num + fish_num}), pnominee={pnominee}, {i}")
    gprint(pshark_location, rgraph, rdgraph)

    peat_num += fish_num
    # 물고기 대이동
    rgraph, rdgraph, rfishes = moving_fish(pshark_location, rgraph, rdgraph, rfishes)

    print("<2> 물고기 이동")
    gprint(pshark_location, rgraph, rdgraph)

    # 먹을 수 있는 물고기들
    nominee_fish = get_nominee_fish(pshark_location, rgraph, rdgraph)

    # 더이상 먹을 수 있는 물고기가 없으면 끝낸다
    if len(nominee_fish) == 0:
        print("<3> 끝 -----------------------------", peat_num)
        ate_fish.append(peat_num)
        return

    for j in range(len(nominee_fish)):
        cycle(j, nominee_fish, peat_num, rgraph, rdgraph, rfishes)


data = []
graph = []
dgraph = []
fishes = []
ate_fish = []

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
        fishes.append([data[x][2 * y], x, y])
    graph.append(gtemp)
    dgraph.append(dtemp)

fishes.sort()

cycle(0, [[graph[0][0], 0, 0]], 0, graph, dgraph, fishes)
print(ate_fish)
print(max(ate_fish))
