from collections import deque


# def gprint(data):
#     for x in range(len(data)):
#         for y in range(len(data)):
#             print(data[x][y], end=" ")
#         print()


def solution(n, start, end, roads, traps):
    answer = []
    edge = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dist = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for road in roads:
        a, b, cost = road
        edge[a][b] = 1
        dist[a][b] = cost
        dist[b][a] = cost

    q = deque([[start, 0]])  # 시작지점, 시간

    while q:
        node, time = q.popleft()

        if node == end:
            answer.append(time)
            continue

        if visited[node] > 2 and visited[node] != 0:
            continue

        for n_node in range(n + 1):

            # node와 연결된 노드 n_node
            if edge[node][n_node] == 1:

                cost = dist[node][n_node]

                # 그다음 방문할 노드 n_node 가 함정이라면
                if n_node in traps:
                    for j in range(n + 1):

                        # 함정과 연결된 경로를 모두 뒤집는다
                        if edge[n_node][j] == 1:
                            edge[n_node][j] = 0
                            edge[j][n_node] = 1
                        elif edge[j][n_node] == 1:
                            edge[j][n_node] = 0
                            edge[n_node][j] = 1

                q.append([n_node, cost + time])
                visited[n_node] += 1

    print(answer)
    if len(answer) == 0:
        return 0
    return min(answer)


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
