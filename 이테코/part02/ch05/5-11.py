from collections import deque

n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

for _ in range(n):
    graph.append(list(map(int, input())))


def bsf(i, j):
    global count
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            kx = i + dx[k]
            ky = j + dy[k]

            if kx < 0 or ky < 0 or kx >= n or ky >= m:
                continue

            if graph[kx][ky] == 0:
                continue

            if graph[kx][ky] == 1:
                graph[kx][ky] = graph[i][j] + 1
                queue.append((kx, ky))
    return


bsf(0, 0)
print(graph[n - 1][m - 1])

for _ in graph:
    print(_)

"""
5 6
101010
111111
000001
111111
111111

8 7
1001111
1001011
1111011
0000011
1111111
1000001
1111111
1111111

3 3
110
010
011
"""
