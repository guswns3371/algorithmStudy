from collections import deque
import copy


def turning_head(to, direct):
    # immutable object (int, float, str, tuples)가 함수의 인자로 넘어가면
    # Call by Value 로 넘어가 원래값을 변경시키지 않는다
    # 왼쪽으로 90 꺽기
    if to == "L":
        if direct == _UP:
            return _LEFT
        elif direct == _DOWN:
            return _RIGHT
        elif direct == _RIGHT:
            return _UP
        elif direct == _LEFT:
            return _DOWN
    # 오른쪽으로 90 꺽기
    elif to == "D":
        if direct == _UP:
            return _RIGHT
        elif direct == _DOWN:
            return _LEFT
        elif direct == _RIGHT:
            return _DOWN
        elif direct == _LEFT:
            return _UP


def next_head(head, direct):
    # mutable object (list, dict, set)가 함수의 인자로 넘어가면
    # Call by Reference 로 넘어가 head 값을 변경시킨다. 그래서 deepcopy
    return_head = copy.deepcopy(head)
    if direct == _UP:
        return_head[0] -= 1
    elif direct == _DOWN:
        return_head[0] += 1
    elif direct == _RIGHT:
        return_head[1] += 1
    elif direct == _LEFT:
        return_head[1] -= 1

    return return_head


def print_snake(snake, board):
    return_board = copy.deepcopy(board)
    return_snake = copy.deepcopy(snake)
    i = 0
    j = 0
    while return_snake:
        i, j = return_snake.popleft()
        return_board[i][j] = 2
    return_board[i][j] = 3
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if return_board[i][j] == 0:
                print("□", end=" ")
            elif return_board[i][j] == 1:
                print("◬", end=" ")
            elif return_board[i][j] == 2:
                print("■", end=" ")
            elif return_board[i][j] == 3:
                print("◪", end=" ")
        print()


N = int(input())
K = int(input())
board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

L = int(input())
# 뱀의 방향 전환 정보
turn = deque([])
for _ in range(L):
    x, c = input().split()
    turn.append([x, c])

# 뱀의 몸통 : 큐를 사용한다
snake = deque([[1, 1]])

# 상하좌우
_UP = 0
_DOWN = 1
_RIGHT = 2
_LEFT = 3
direction = _RIGHT

# 게임 시간
time = 0

print_snake(snake, board)
print("---------------------------------")

while snake:
    time += 1
    start = snake[0]

    new_head = next_head(start, direction)

    # 게임이 끝남
    if new_head[0] < 1 or new_head[0] > N or new_head[1] < 1 or new_head[1] > N:
        print(new_head)
        break

    # 만약 다음칸에 뱀의 몸이 있으면 게임이 끝나게 됨
    if new_head in snake:
        break

    # 머리를 다음칸에 위치시킴
    snake.appendleft(new_head)
    # 사과가 있을 경우
    if board[new_head[0]][new_head[1]] == 1:
        # 사과를 없앤다
        board[new_head[0]][new_head[1]] = 0
        print("💥!전방에 사과!", end=" ")
    #  사과가 없을 경우
    elif board[new_head[0]][new_head[1]] == 0:
        # 꼬리를 없앤다
        snake.pop()

    print(f"[{time}초] 시작={start}", end=" ")
    print(f"= <{direction}방향> => {new_head}", snake)
    print_snake(snake, board)

    # 방향 전환 정보로 이동방향 전환하기
    while turn:
        x, c = turn[0]
        # x초가 끝난 뒤에 방향을 튼다
        if time == int(x):
            turn.popleft()
            # 이동방향 갱신
            direction = turning_head(c, direction)
            print(f"💥!턴! {c}")
        break

print(time)
