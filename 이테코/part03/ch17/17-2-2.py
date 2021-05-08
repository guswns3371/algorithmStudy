from collections import deque
import random
import numpy as np
import timeit


def find_chart(graph, start, biggers, others):
    visited = [0] * (n + 1)
    dist = [INF] * (n + 1)
    q = deque([[0, start]])

    dist[start] = 0
    visited[start] = 1

    while q:
        cost, now = q.popleft()

        for node in graph[now]:
            if visited[node] != 1:
                dist[node] = min(dist[node], dist[now] + 1)
                q.append([dist[node], node])
                visited[node] = 1

    dist[0] = -1
    for ii in range(1, n + 1):
        if ii == start:
            continue

        if dist[ii] < INF:
            biggers[start].append(ii)
        else:
            others[start].append(ii)


INF = int(1e9)
while True:
    n, m = random.randint(2, 10), random.randint(2, 20)
    print(f"{n} {m}")

    temp_lst = [i + 1 for i in range(n)]

    # random_array = np.random.randint(1, n, size=(m, 2)).tolist()

    random_array = [[]]
    while len(random_array) < m:
        sample_list = random.sample(temp_lst, k=2)
        if sample_list not in random_array:
            if sorted(sample_list) not in random_array:
                if sorted(sample_list, reverse=True) not in random_array:
                    random_array.append(sample_list)
    random_array.remove([])

    for rd in random_array:
        for rrd in rd:
            print(rrd, end=" ")
        print()
    print("=============")

    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for lst in random_array:
        # A에서 B로 가는 비용을 1로 설정
        a, b = lst
        graph[a][b] = 1

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = 0
    # 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            result += 1

    print("동빈 : ", result)

    graph = [[] for _ in range(n + 1)]
    biggers = [[] for _ in range(n + 1)]
    others = [[] for _ in range(n + 1)]
    know = 0

    for lst in random_array:
        a, b = lst
        graph[a].append(b)

    for i in range(n):
        find_chart(graph, i + 1, biggers, others)

    for i in range(n):
        student = i + 1
        # print(f"{student}번 학생 보다 큰 놈들 : {biggers[student]}")
        # print(f"그 이외의 놈들 : {others[student]}")
        dunno = len(others[student])
        for other in others[student]:
            if student in biggers[other]:
                dunno -= 1

        if dunno == 0:
            know += 1
            # print(f"{student} 학생 순위 정확히 앎 🔥")
        else:
            # print(f"{student} 학생 순위 모름, 확실치 않은 핵생수={dunno}")
            pass

    print("현준 : ", know)

    if know == result:
        print("정답!")
    else:
        print("오답!")
        break
    print("====================================================")
