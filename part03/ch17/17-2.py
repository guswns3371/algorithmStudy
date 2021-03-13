INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("*",end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""