import heapq
import sys
input = sys.stdin.readline

# 도시의 개수, 통로의 개수, 보내고자 하는 도시
n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    # x->y 통로로 메시지가 전달되는 시간 = z시간
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # start->start 로 메시지가는 시간 = 0시간
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # distance 에 저장된 최단 거리보다 지금 방문한 노드 now 까지의 거리 dist가 크면
        # 가차없이 나가리
        if dist > distance[now]:
            continue

        # i[0] = y노드
        # i[1] = z시간
        # now -> i[0] 통로로 메시지가 가는 시간 = i[1]시간
        for i in graph[now]:
            # cost : start->now 의 최단거리 + now-> i[0] 의 최단거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
num_of_city = 0

# enumerate(리스트, index 값에 더할 수)
''' builtins.py
def __init__(self, iterable, start=0): # known special case of enumerate.__init__
    """ Initialize self.  See help(type(self)) for accurate signature. """
    pass
'''
for i, d in enumerate(distance, 1):
    if d == INF:
        distance[i - 1] = -1
    else:
        # start 노드도 포함됨 -> 나중에 한개 뺴줘야 한다
        num_of_city += 1

total_time = max(distance)

print(num_of_city - 1, total_time)
'''
3 2 1
1 2 4
1 3 2
'''
