from collections import deque
import heapq
import random
import numpy as np
import timeit


def my_hide(input_graph):
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)
    for ip in input_graph:
        a, b = ip
        # 양방향 통로 , 모든 통로의 가중치를 1로 둔다
        graph[a].append(b)
        graph[b].append(a)

    dist[1] = 0
    q = deque([[dist[1], 1]])

    while q:
        cost, now = q.popleft()

        for node in graph[now]:

            if dist[node] <= dist[now] + 1 and dist[node] != INF:
                continue
            dist[node] = min(dist[node], dist[now] + 1)
            q.append([dist[node], node])

    dist[0] = -1
    # print("현준 : ", dist)

    barn_dist = max(dist)
    barn_num = dist.index(barn_dist)
    barn_count = dist.count(barn_dist)

    return barn_num, barn_dist, barn_count


def dijkstra(distance, start, graph):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def dong_hide(input_graph):
    # 시작 노드를 1번 헛간으로 설정
    start = 1
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    # 모든 간선 정보를 입력받기
    for ip in input_graph:
        a, b = ip
        # a번 노드와 b번 노드의 이동 비용이 1이라는 의미(양방향)
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    # 다익스트라 알고리즘을 수행
    dijkstra(distance, start, graph)

    # 가장 최단 거리가 먼 노드 번호(동빈이가 숨을 헛간의 번호)
    max_node = 0
    # 도달할 수 있는 노드 중에서, 가장 최단 거리가 먼 노드와의 최단 거리
    max_distance = 0
    # 가장 최단 거리가 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
    result = []

    for i in range(1, n + 1):
        if max_distance < distance[i]:
            max_node = i
            max_distance = distance[i]
            result = [max_node]
        elif max_distance == distance[i]:
            result.append(i)


    return max_node, max_distance, len(result)


INF = int(1e9)

while True:
    # n, m = random.randint(2, 20000), random.randint(1, 50000)
    n, m = random.randint(2, 10), random.randint(1, 15)
    input_graph = np.random.randint(1, n, size=(m, 2)).tolist()

    print("=========시작==========")
    print(f"n={n}, m={m}")
    print(f"graph : {input_graph}")

    start_time = timeit.default_timer()  # 시작 시간 체크
    result1 = dong_hide(input_graph)
    terminate_time = timeit.default_timer()  # 종료 시간 체크
    print("동빈 : ", result1, " %f초 걸렸습니다." % (terminate_time - start_time))

    start_time = timeit.default_timer()  # 시작 시간 체크
    result2 = my_hide(input_graph)
    terminate_time = timeit.default_timer()  # 종료 시간 체크
    print("현준 : ", result2, " %f초 걸렸습니다." % (terminate_time - start_time))

    if result1 == result2:
        print("맞음")
    else:
        print("틀림")
        break
    print("==========끝==========")

    print()
