"""
적록색약 https://www.acmicpc.net/problem/10026
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
agraph = []
bgraph = []
avisited = [[0 for _ in range(n)] for _ in range(n)]
bvisited = [[0 for _ in range(n)] for _ in range(n)]
acount = 0
bcount = 0
for _ in range(n):
    data = list(input())
    agraph.append(data)
    bgraph.append([('G' if c == 'G' or c == 'R' else c) for c in data])

# R=ord('R'), G=ord('G'), B=ord('B'), 방문안한 곳 = 0
for x in range(n):
    for y in range(n):
        # 정상인

        if avisited[x][y] == 0:
            acount += 1
            aq = deque([[x, y]])
            color = ord(agraph[x][y])
            avisited[x][y] = color
            while aq:
                ax, ay = aq.popleft()
                for i in range(4):
                    xx = ax + dx[i]
                    yy = ay + dy[i]

                    if 0 <= xx < n and 0 <= yy < n:
                        if avisited[xx][yy] == 0 and ord(agraph[xx][yy]) == color:
                            avisited[xx][yy] = color
                            aq.append([xx, yy])
        # 적록색약인
        if bvisited[x][y] == 0:
            bcount += 1
            bq = deque([[x, y]])
            color = ord(bgraph[x][y])
            bvisited[x][y] = color
            while bq:
                bx, by = bq.popleft()
                for i in range(4):
                    xx = bx + dx[i]
                    yy = by + dy[i]

                    if 0 <= xx < n and 0 <= yy < n:
                        if bvisited[xx][yy] == 0 and ord(bgraph[xx][yy]) == color:
                            bvisited[xx][yy] = color
                            bq.append([xx, yy])
print(acount, bcount)
