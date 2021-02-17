"""
from collections import deque


def move_location(m_loc_xy, m_direct):
    tx, ty = m_loc_xy
    if m_direct == UP:
        tx -= 1
    elif m_direct == DOWN:
        tx += 1
    elif m_direct == RIGHT:
        ty += 1
    elif m_direct == LEFT:
        ty -= 1
    return [tx, ty]


# 로봇이 가로로 되어있는지 확인
def check_horizontal(p_robot):
    pa_loc, pb_loc = p_robot
    px = pa_loc[0] - pb_loc[0]
    py = pa_loc[1] - pb_loc[1]

    if px == 0 and py == -1:
        # 로봇이 가로 형태인 경우
        return True
    elif px == -1 and py == 0:
        # 로봇이 세로 형태인 경우
        return False


# 현재 위치가 가능한 위치인지 확인
def check_valid_location(p_loc_xy, p_board):
    global arrived
    px, py = p_loc_xy
    if px < 0 or py < 0 or px >= n or py >= n:
        return False
    if p_board[px][py] == 1:
        return False
    if p_loc_xy == [n - 1, n - 1]:
        arrived = True
        return True
    return True


# 현재 로봇 위치가 가능한 위치인지 확인
def check_robot_location(p_loc, p_board):
    pa_loc, pb_loc = p_loc
    if not check_valid_location(pa_loc, p_board):
        return False
    if not check_valid_location(pb_loc, p_board):
        return False
    return True


def rotate_robot(p_board, p_loc, p_direct):
    pa_loc, pb_loc = p_loc

    if check_horizontal(p_loc):
        # 로봇이 가로형태인 경우
        if p_direct == LD:
            # 2번쨰 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([pb_loc, tmp_loc])

        elif p_direct == RD:
            # 1번째 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([pa_loc, tmp_loc])

        elif p_direct == LU:
            # 2번째 칸을 기준으로 위,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([tmp_loc, pb_loc])

        elif p_direct == RU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([tmp_loc, pa_loc])
    else:
        # 로봇이 세로형태인 경우
        if p_direct == LD:
            # 2번쨰 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pa_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([tmp_loc, pb_loc])
        elif p_direct == RD:
            # 2번째 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([pb_loc, tmp_loc])
        elif p_direct == LU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([tmp_loc, pa_loc])
        elif p_direct == RU:
            # 1번째 칸을 기준으로 위,오른쪽으로로 회전
            tmp_loc = move_location(pb_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                return None

            p_loc = ([pa_loc, tmp_loc])
    return p_loc


def move_robot(p_board, p_loc, px, py):
    pa_loc, pb_loc = p_loc
    ra = [pa_loc[0] + px, pa_loc[1] + py]
    rb = [pb_loc[0] + px, pb_loc[1] + py]
    tmp_robot = [ra, rb]

    if not check_robot_location(tmp_robot, p_board):
        return None

    return tmp_robot


def visit(v_visited, v_loc):
    v_visited.append(v_loc)


def bfs(graph, start, visited):
    global arrived
    queue = deque([[0, start]])
    visit(visited, start)

    while queue:
        m_time, m_loc = queue.popleft()
        # 상하좌우 이동
        for i in range(4):
            moved = move_robot(graph, m_loc, dx[i], dy[i])
            if moved is not None and moved not in visited:
                queue.append([m_time + 1, moved])
                visit(visited, moved)
                if arrived:
                    return m_time + 1

                for j in range(4):
                    mv_rotated = rotate_robot(graph, moved, j)
                    if mv_rotated is not None and mv_rotated not in visited:
                        queue.append([m_time + 2, mv_rotated])
                        visit(visited, mv_rotated)
                        if arrived:
                            return m_time + 2


def solution(board):
    global n
    n = len(board)

    robot = [[0, 0], [0, 1]]
    visited = []

    return bfs(board, robot, visited)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
LD, RD, LU, RU = 0, 1, 2, 3
UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
arrived = False
n = -1

s_board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(s_board))"""

from collections import deque


def print_graph(p_graph, p_robot):
    for pi in range(n):
        for pj in range(n):
            if [pi, pj] in p_robot:
                print("◈", end=" ")
                continue

            if p_graph[pi][pj] == 1:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()
    print()


def move_location(m_loc_xy, m_direct):
    tx, ty = m_loc_xy
    if m_direct == UP:
        tx -= 1
    elif m_direct == DOWN:
        tx += 1
    elif m_direct == RIGHT:
        ty += 1
    elif m_direct == LEFT:
        ty -= 1
    return [tx, ty]


# 로봇이 가로로 되어있는지 확인
def check_horizontal(p_robot):
    pa_loc, pb_loc = p_robot
    px = pa_loc[0] - pb_loc[0]
    py = pa_loc[1] - pb_loc[1]

    if px == 0 and py == -1:
        # 로봇이 가로 형태인 경우
        print("가로모드")
        return True
    elif px == -1 and py == 0:
        # 로봇이 세로 형태인 경우
        print("세로모드")
        return False


# 현재 위치가 가능한 위치인지 확인
def check_valid_location(p_loc_xy, p_board):
    global arrived, n
    px, py = p_loc_xy
    if px < 0 or py < 0 or px >= n or py >= n:
        print("로봇 : 지도밖 불가능", p_loc_xy)
        return False
    if p_board[px][py] == 1:
        print("로봇 : 벽 불가능", p_loc_xy)
        return False
    if p_loc_xy == [n - 1, n - 1]:
        print("도착!!!")
        arrived = True
        return True
    return True


# 현재 로봇 위치가 가능한 위치인지 확인
def check_robot_location(p_loc, p_board):
    pa_loc, pb_loc = p_loc
    if not check_valid_location(pa_loc, p_board):
        return False
    if not check_valid_location(pb_loc, p_board):
        return False
    return True


def rotate_robot(p_board, p_loc, p_direct):
    pa_loc, pb_loc = p_loc

    if check_horizontal(p_loc):
        # 로봇이 가로형태인 경우
        if p_direct == LD:
            # 2번쨰 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([pb_loc, tmp_loc])
            print("회전 가능!", p_loc)

        elif p_direct == RD:
            # 1번째 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([pa_loc, tmp_loc])
            print("회전 가능!", p_loc)

        elif p_direct == LU:
            # 2번째 칸을 기준으로 위,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([tmp_loc, pb_loc])
            print("회전 가능!", p_loc)

        elif p_direct == RU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([tmp_loc, pa_loc])
            print("회전 가능!", p_loc)
    else:
        # 로봇이 세로형태인 경우
        if p_direct == LD:
            # 2번쨰 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pa_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([tmp_loc, pb_loc])
            print("회전 가능!", p_loc)
        elif p_direct == RD:
            # 2번째 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([pb_loc, tmp_loc])
            print("회전 가능!", p_loc)
        elif p_direct == LU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, LEFT)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([tmp_loc, pa_loc])
            print("회전 가능!", p_loc)
        elif p_direct == RU:
            # 1번째 칸을 기준으로 위,오른쪽으로로 회전
            tmp_loc = move_location(pb_loc, RIGHT)
            if not check_valid_location(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_valid_location(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_loc = ([pa_loc, tmp_loc])
            print("회전 가능!", p_loc)
    return p_loc


def move_robot(p_board, p_loc, px, py):
    pa_loc, pb_loc = p_loc
    ra = [pa_loc[0] + px, pa_loc[1] + py]
    rb = [pb_loc[0] + px, pb_loc[1] + py]
    tmp_robot = [ra, rb]

    if not check_robot_location(tmp_robot, p_board):
        return None

    print("로봇 이동", p_loc)
    return tmp_robot


def visit(v_visited, v_loc):
    v_visited.append(v_loc)


def bfs(graph, start, visited):
    global arrived
    queue = deque([[0, start]])
    visit(visited, start)

    while queue:
        m_time, m_loc = queue.popleft()
        print("popleft : ", m_time, "초")
        print_graph(graph, m_loc)

        # 상하좌우 이동
        for i in range(4):
            print(dm[i], "이동", m_time + 1, "초")
            moved = move_robot(graph, m_loc, dx[i], dy[i])

            if moved is not None and moved not in visited:
                print_graph(graph, moved)
                if arrived:
                    return m_time + 1
                queue.append([m_time + 1, moved])
                visit(visited, moved)

                for j in range(4):
                    print(dr[j], "회전", m_time + 2, "초")
                    mv_rotated = rotate_robot(graph, moved, j)

                    if mv_rotated is not None and mv_rotated not in visited:
                        print_graph(graph, mv_rotated)
                        if arrived:
                            return m_time + 2
                        queue.append([m_time + 2, mv_rotated])
                        visit(visited, mv_rotated)


def solution(board):
    global n
    n = len(board)

    robot = [[0, 0], [0, 1]]
    visited = []

    return bfs(board, robot, visited)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
LD, RD, LU, RU = 0, 1, 2, 3
UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
dm = ["UP", "DOWN", "RIGHT", "LEFT"]
dr = ["LD", "RD", "LU", "RU"]
arrived = False
n = -1

s_board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
# s_board = [[0 for _ in range(4)] for _ in range(4)]
print(solution(s_board))
