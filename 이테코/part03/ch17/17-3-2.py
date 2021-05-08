from collections import deque
import heapq
import random
import numpy as np


def my_searching(n, cost_graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([])
    dist = [[INF] * n for _ in range(n)]

    dist[0][0] = cost_graph[0][0]
    q.append([0, 0])

    while q:
        nx, ny = q.popleft()
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                continue

            if dist[xx][yy] <= dist[nx][ny] + cost_graph[xx][yy] and dist[xx][yy] != INF:
                continue

            q.append([xx, yy])
            dist[xx][yy] = min(dist[xx][yy], dist[nx][ny] + cost_graph[xx][yy])

    print("현준")
    for d in dist:
        for dd in d:
            print(dd, end=" ")
        print()
    print("==============")

    return dist[n - 1][n - 1]


def dongbin_search(n, graph):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0  # 시작 위치는 (0, 0)
    # 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘을 수행
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print("동빈")
    for d in distance:
        for dd in d:
            print(dd, end=" ")
        print()
    print("==============")
    return distance[n - 1][n - 1]


INF = int(1e9)
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     cost_graph = []
#     for _ in range(n):
#         cost_graph.append(list(map(int, input().split())))
#
#     result1 = my_searching(n, cost_graph)
#     result2 = dongbin_search(n, cost_graph)
#     if result1 != result2:
#         print("틀림")
#     else:
#         print("맞음")

while True:
    n = random.randint(2, 11)
    print("n",n)
    cost_graph = np.random.randint(0, 9, size=(n, n)).tolist()
    print("graph")
    for d in cost_graph:
        for dd in d:
            print(dd, end=" ")
        print()
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    result2 = dongbin_search(n, cost_graph)
    result1 = my_searching(n, cost_graph)
    print("현준 : ", result1)
    print("동빈 : ", result2)
    if result1 != result2:
        print("틀림")
        break
    else:
        print("맞음")
    print()
