import heapq
from itertools import combinations


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n, m = map(int, input().split())
graph = []
chicken = []
house = []
result = 1e9

for _ in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            house.append([x, y])
        elif graph[x][y] == 2:
            graph[x][y] = 0
            chicken.append([x, y])

combination = list(combinations(chicken, m))

for combi in combination:
    total_dist = 0

    for hone in house:
        heap = []
        for chick in combi:
            heapq.heappush(heap, get_dist(chick, hone))

        total_dist += heap[0]

    if total_dist < result:
        result = total_dist

print(result)
