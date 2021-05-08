from collections import deque


def print_graph(graph):
    gn = len(graph)
    print("----------")
    for i in range(gn):
        for j in range(gn):
            print(graph[i][j], end=" ")
        print()
    print("----------")


def moving(union):
    num_pop = 0
    for u in union:
        x, y = u
        num_pop += A[x][y]

    new_pop = num_pop // len(union)

    while union:
        x, y = union.pop(0)
        A[x][y] = new_pop


def open_gate(location_a, location_b):
    if L <= abs(A[location_a[0]][location_a[1]] - A[location_b[0]][location_b[1]]) <= R:
        return True
    return False


# 각 국가는 하나의 연합이다
# bfs를 이용하여 연합의 각 칸의 인구수를 구한다
# union은 [x좌표,y좌표] 형태이다.
def make_union(start, visited):
    ux, uy = start[0], start[1]
    queue = deque([[ux, uy]])
    visited[ux][uy] = 1
    union = [[ux, uy]]
    while queue:
        nx, ny = queue.popleft()
        # 현재 방문한 나라(nx,ny)와 상하좌우로 인접한 나라(xx,yy)를 탐색한다
        for ii in range(4):
            xx = nx + dx[ii]
            yy = ny + dy[ii]

            # 범위를 벗어난 경우, 방문한 적이 있는 경우 continue
            if xx < 0 or yy < 0 or xx >= n or yy >= n or visited[xx][yy] == 1:
                continue

            # 공유하는 국경선을 연다.
            if open_gate([nx, ny], [xx, yy]):
                # 큐에 삽입
                queue.append([xx, yy])
                union.append([xx, yy])
                # 방문처리
                visited[xx][yy] = 1

    return union


n, L, R = map(int, input().split())
A = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    A.append(list(map(int, input().split())))

# 하루 동안의 인구이동 과정
move = 0
keep_going = True
while keep_going:    # 연합 리스트
    t_union_list = []
    # 방문체크 리스트
    visited = [[0 for _ in range(n)] for _ in range(n)]
    keep_going = False

    # 0,0 부터 차례대로 국가를 방문
    for i in range(n):
        for j in range(n):
            t_union = make_union([i, j], visited)

            # 연합이 만들어진 경우
            if len(t_union) > 1:
                t_union_list.append(t_union)

    for tu in t_union_list:
        print(tu)
        keep_going = True
        moving(tu)

    if keep_going:
        move += 1
        print_graph(A)


print(move)