from itertools import combinations


def solution(places):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    graph = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    answer = []

    for i in range(5):
        place = places[i]
        for x in range(5):
            for y in range(5):
                graph[i][x][y] = place[x][y]

    for i in range(5):
        # i번쨰 대기실
        room = graph[i]
        people = []
        partitions = []
        blank = []

        for x in range(5):
            for y in range(5):
                if room[x][y] == "P":
                    people.append([x, y])
                elif room[x][y] == "O":
                    blank.append([x, y])
                elif room[x][y] == "X":
                    partitions.append([x, y])

        cases = list(combinations(people, 2))

        ok = True
        for case in cases:
            ax, ay = case[0]
            bx, by = case[1]
            dist = abs(ax - bx) + abs(ay - by)

            # 맨해튼 거리 2보다 크면 통과
            if dist > 2:
                continue

            a_locs = []
            b_locs = []
            ab_locs = []

            if dist == 2:
                for k in range(4):
                    axx = ax + dx[k]
                    ayy = ay + dy[k]

                    bxx = bx + dx[k]
                    byy = by + dy[k]

                    if 0 <= axx < 5 and 0 <= ayy < 5:
                        a_locs.append([axx, ayy])

                    if 0 <= bxx < 5 and 0 <= byy < 5:
                        b_locs.append([bxx, byy])

                for a_one in a_locs:
                    if a_one in b_locs:
                        ab_locs.append(a_one)

                for ab_loc in ab_locs:
                    if room[ab_loc[0]][ab_loc[1]] == "O":
                        ok = False

            elif dist == 1:
                ok = False

        if ok:
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
