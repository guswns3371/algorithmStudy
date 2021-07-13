"""
알파벳 https://www.acmicpc.net/problem/1987
ord() : 문자열을 아스키코드로 반환할 수 있는 함수
ord('A') == 65
ord('Z') == 90

dfs 6536ms
bfs 5332ms
"""
from collections import deque


def recursive(start, count):
    global max_num, data

    x, y = start
    max_num = max(max_num, count)

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if not (0 <= xx < r and 0 <= yy < c):
            continue
        if graph[xx][yy] in data:
            continue

        data.append(graph[xx][yy])
        recursive([xx, yy], count + 1)
        data.remove(graph[xx][yy])


def queue(start):
    answer = 1
    a, b = start
    q = deque([(a, b, graph[a][b])])
    while q:
        x, y, string = q.pop()  # popleft()가 아님
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if not (0 <= xx < r and 0 <= yy < c):
                continue
            if graph[xx][yy] in string:
                continue

            q.append((xx, yy, string + graph[xx][yy]))
            answer = max(answer, len(string) + 1)
    return answer


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
r, c = map(int, input().split())
data = []
graph = []
max_num = -int(1e9)
for _ in range(r):
    graph.append(list(input()))

data.append(graph[0][0])
# dfs([0, 0], 1)
# print(max_num)
print(queue([0, 0]))
