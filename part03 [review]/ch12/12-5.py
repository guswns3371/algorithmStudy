from collections import deque


def gprint():
    for gx in range(n):
        for gy in range(n):
            if [gx, gy] in snake:
                print("■", end=" ")
            else:
                if graph[gx][gy] == 1:
                    print("◎", end=" ")
                else:
                    print("□", end=" ")
        print()
    print()


def get_direct_index(di, data):
    if data == "L":
        if di == 0:
            return 3
        else:
            return di - 1
    else:
        if di == 3:
            return 0
        else:
            return di + 1


n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
direct = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

for _ in range(int(input())):
    x, c = input().split()
    direct.append([x, c])

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0

# 뱀
snake = deque([[0, 0]])
# 뱀의 이동 방향
sd = 1

while True:
    # 뱀의 머리
    sx, sy = snake[0]

    # 머리가 위치할 곳
    xx = sx + dx[sd]
    yy = sy + dy[sd]

    # 미래의 머리 위치가 유효한지 확인
    if xx < 0 or yy < 0 or xx >= n or yy >= n or [xx, yy] in snake:
        time += 1
        break

    # 몸을 늘린다
    snake.appendleft([xx, yy])

    # 미래의 머리 위치에 사과없으면 꼬리를 옮긴다
    if graph[xx][yy] == 1:
        graph[xx][yy] = 0
    else:
        snake.pop()

    # 시간 1초 경과
    time += 1

    # 이동방향 바꾸기
    if direct:
        dt, dd = direct[0]
        if int(dt) == time:
            sd = get_direct_index(sd, dd)
            direct.pop(0)

print(time)
