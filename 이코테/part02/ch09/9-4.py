# 플로이드 워셜 알고리즘

INF = int(1e9)
n, m = map(int, input().split())
start = 1

# graph : 각 노드마다 연결되어있는 노드를 담는 리스트
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 각 노드마다 자신으로 가는 비용 = 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # a,b 노드가 서로 이어져 있다.
    a, b = map(int, input().split())
    # 이웃한 노드로 가는 시간 = 1
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

'''
A는 1 -> K -> X 의 경로를 거친다
D1k = min(D1k, D1y + Dyk)
Dkx = min(Dkx, Dky + Dyx)
result = D1k + Dkx
만약, x번쨰 회사에 도달할 수 없으면(result >= INF 인 경우) : -1 출력  
'''

for y in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][y] + graph[y][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("*", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''
