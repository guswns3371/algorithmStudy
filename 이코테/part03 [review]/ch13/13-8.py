from collections import deque


def next_pos(n, board, robot):
    ax, ay, bx, by = robot[0][0], robot[0][1], robot[1][0], robot[1][1]
    positions = []
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        xxa, yya, xxb, yyb = ax + dx[i], ay + dy[i], bx + dx[i], by + dy[i]
        if min(xxa, yya, xxb, yyb) < 0 or max(xxa, yya, xxb, yyb) >= n:
            continue
        if board[xxa][yya] == 1 or board[xxb][yyb] == 1:
            continue
        positions.append(sorted([[xxa, yya], [xxb, yyb]]))

    # 회전
    if ax == bx:  # 가로
        for i in [-1, 1]:
            xxa, yya, xxb, yyb = ax + i, ay, bx + i, by
            if min(xxa, yya, xxb, yyb) < 0 or max(xxa, yya, xxb, yyb) >= n:
                continue
            if board[xxa][yya] == 1 or board[xxb][yyb] == 1:
                continue
            positions.append(sorted([[ax, ay], [xxa, yya]]))
            positions.append(sorted([[bx, by], [xxb, yyb]]))
    elif ay == by:  # 세로
        for i in [-1, 1]:
            xxa, yya, xxb, yyb = ax, ay + i, bx, by + i
            if min(xxa, yya, xxb, yyb) < 0 or max(xxa, yya, xxb, yyb) >= n:
                continue
            if board[xxa][yya] == 1 or board[xxb][yyb] == 1:
                continue
            positions.append(sorted([[ax, ay], [xxa, yya]]))
            positions.append(sorted([[bx, by], [xxb, yyb]]))

    return positions


def solution(board):
    n = len(board)
    robot = [[0, 0], [0, 1]]
    rvisited = [robot]
    q = deque([[0, robot]])  # 시간, 로봇 1부분, 로봇 2부분

    while q:
        rtime, robot = q.popleft()
        if [n - 1, n - 1] in robot:
            return rtime

        for pos in next_pos(n, board, robot):
            if pos not in rvisited:
                rvisited.append(pos)
                q.append([rtime + 1, pos])
