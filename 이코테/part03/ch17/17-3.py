from collections import deque
import heapq


def searching(start):
    q = []
    dist = [[INF] * n for _ in range(n)]

    x, y = start
    dist[x][y] = cost_graph[x][y]
    heapq.heappush(q, (cost_graph[0][0], 0, 0))

    while q:
        cost, nx, ny = heapq.heappop(q)
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                continue

            if dist[xx][yy] < cost + cost_graph[xx][yy] and dist[xx][yy] != INF:
                continue

            dist[xx][yy] = min(dist[xx][yy], cost + cost_graph[xx][yy])
            heapq.heappush(q, (dist[xx][yy], xx, yy))

    for d in dist:
        for dd in d:
            print(dd, end=" ")
        print()
    print("==============")


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     cost_graph = []
#     for _ in range(n):
#         cost_graph.append(list(map(int, input().split())))
#
#     searching(n, cost_graph)

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
cost_graph = []
for _ in range(n):
    cost_graph.append(list(map(int, input().split())))

searching([0, 0])

"""
3
5 5 4
3 9 1
3 2 7

5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5

7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
