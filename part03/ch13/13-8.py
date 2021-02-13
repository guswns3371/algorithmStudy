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


def move_location(m_location, m_direction):
    tx, ty = m_location
    if m_direction == UP:
        tx -= 1
    elif m_direction == DOWN:
        tx += 1
    elif m_direction == RIGHT:
        ty += 1
    elif m_direction == LEFT:
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


def check_possibility(p_location, p_board):
    global arrived
    px, py = p_location
    if px < 0 or py < 0 or px >= n or py >= n:
        print("로봇 : 지도밖 불가능", p_location)
        return False
    if p_board[px][py] == 1:
        print("로봇 : 벽 불가능", p_location)
        return False
    if p_location == [n - 1, n - 1]:
        print("도착!!!")
        arrived = True
        return True
    return True


# 현재 로봇 위치가 가능한 위치인지 확인
def check_robot_location(p_location, p_board):
    pa_loc, pb_loc = p_location
    if not check_possibility(pa_loc, p_board):
        return False
    if not check_possibility(pb_loc, p_board):
        return False
    return True


def rotate_robot(p_board, p_robot, p_direction):
    pa_loc, pb_loc = p_robot

    if check_horizontal(p_robot):
        # 로봇이 가로형태인 경우
        if p_direction == LD:
            # 2번쨰 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, DOWN)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([pb_loc, tmp_loc])
            print("회전 가능!", p_robot)

        elif p_direction == RD:
            # 1번째 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, DOWN)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([pa_loc, tmp_loc])
            print("회전 가능!", p_robot)

        elif p_direction == LU:
            # 2번째 칸을 기준으로 위,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, UP)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, RIGHT)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([tmp_loc, pb_loc])
            print("회전 가능!", p_robot)

        elif p_direction == RU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, UP)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, LEFT)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([tmp_loc, pa_loc])
            print("회전 가능!", p_robot)
    else:
        # 로봇이 세로형태인 경우
        if p_direction == LD:
            # 2번쨰 칸을 기준으로 아래,왼쪽으로 회전
            tmp_loc = move_location(pa_loc, LEFT)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([tmp_loc, pb_loc])
            print("회전 가능!", p_robot)
        elif p_direction == RD:
            # 2번째 칸을 기준으로 아래,오른쪽으로 회전
            tmp_loc = move_location(pa_loc, RIGHT)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, DOWN)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([pb_loc, tmp_loc])
            print("회전 가능!", p_robot)
        elif p_direction == LU:
            # 1번째 칸을 기준으로 위,왼쪽으로 회전
            tmp_loc = move_location(pb_loc, LEFT)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([tmp_loc, pa_loc])
            print("회전 가능!", p_robot)
        elif p_direction == RU:
            # 1번째 칸을 기준으로 위,오른쪽으로로 회전
            tmp_loc = move_location(pb_loc, RIGHT)
            if not check_possibility(tmp_loc, p_board):
                print("벽: 회전 불가능")
                return None

            tmp_loc = move_location(tmp_loc, UP)
            if not check_possibility(tmp_loc, p_board):
                print("회전 불가능", tmp_loc)
                return None

            p_robot = ([pa_loc, tmp_loc])
            print("회전 가능!", p_robot)
    return p_robot


def move_robot(p_board, p_robot, px, py):
    location_a, location_b = p_robot
    ra = [location_a[0] + px, location_a[1] + py]
    rb = [location_b[0] + px, location_b[1] + py]
    tmp_robot = [ra, rb]

    if not check_robot_location(tmp_robot, p_board):
        return None

    print("로봇 이동", p_robot)
    return tmp_robot


def solution(board):
    global n
    time = 0
    n = len(board)
    robot = [[0, 0], [0, 1]]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    print_graph(board, robot)
    print("===========================<상하좌우 이동>")
    for i in range(4):
        print(dm[i])
        i_robot = move_robot(board, robot, dx[i], dy[i])
        if i_robot is not None:
            print_graph(board, i_robot)

    print("===========================<회전>")
    for i in range(4):
        print(dr[i])
        i_robot = rotate_robot(board, robot, i)
        if i_robot is not None:
            print_graph(board, i_robot)

    return time


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
