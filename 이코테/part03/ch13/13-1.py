from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, start, visited):
    # 큐에 start노드 삽입
    queue = deque([start])
    # 방문처리
    visited[start] = True
    distance[start] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # 현재 방문 노드 now와 연결된 노드i의 거리를 갱신한다.
                # if i != x:
                distance[i] = min(distance[i], distance[now] + 1)
                # 만약 노드now에서 노드x로 가는경우 최단거리를 0으로 설정
                # else:
                #     distance[i] = 0


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 시작 노드로부터 거리를 저장하는 리스트
distance = [int(1e9)] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(graph, x, visited)
print(distance)
# 최단 거리가 k인 도시 번호 탐색
flag = True
for d in range(len(distance)):
    if distance[d] == k:
        print(d)
        flag = False

if flag:
    print(-1)
