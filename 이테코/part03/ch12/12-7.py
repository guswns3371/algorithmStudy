import itertools


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n, m = map(int, input().split())
city = []
house = []
chicken_house = []
# chick_dist[i] : [chicken[i] 와 집 사이의 거리..] 정보의 배열
chick_dist = []
INF = int(1e9)

for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i + 1, j + 1])
        elif city[i][j] == 2:
            chicken_house.append([i + 1, j + 1])

print("house", house)
temp_list = [i for i in range(len(chicken_house))]
combination = list(itertools.combinations(temp_list, m))
c_list = []
for comb in combination:
    c_list.append(list(comb))

for c in chicken_house:
    dist = []
    for h in house:
        dist.append(distance(h, c))
    chick_dist.append(dist)

for i in range(len(chicken_house)):
    print("치킨집", chicken_house[i], end=" : ")
    print("거리", chick_dist[i])

print("경우의 수", c_list)

min_dist = [INF for _ in range(len(house))]
for i in range(len(c_list)):
    temp_dist = [INF for _ in range(len(house))]
    print(c_list[i], "비교")
    for j in c_list[i]:
        for k in range(len(house)):
            temp_dist[k] = min(temp_dist[k], chick_dist[j][k])
    print("temp_dist", temp_dist, sum(temp_dist), end=" => ")
    if sum(temp_dist) < sum(min_dist):
        min_dist = temp_dist
    print("min_dist", min_dist, sum(min_dist))

print(sum(min_dist))

'''
import heapq
import itertools


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n, m = map(int, input().split())
city = []
house = []
chicken_house = []
# chick_dist[i] : [chicken[i] 와 집 사이의 거리..] 정보의 배열
chick_dist = []
INF = int(1e9)

for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i + 1, j + 1])
        elif city[i][j] == 2:
            chicken_house.append([i + 1, j + 1])

min_dist = [INF for _ in range(len(house))]
temp_list = [i for i in range(len(chicken_house))]
combination = list(itertools.combinations(temp_list, m))
c_list = []
for comb in combination:
    c_list.append(list(comb))

for c in chicken_house:
    dist = []
    for h in house:
        dist.append(distance(h, c))
    chick_dist.append(dist)


for i in range(len(c_list)):
    temp_dist = [INF for _ in range(len(house))]
    for j in c_list[i]:
        for k in range(len(house)):
            temp_dist[k] = min(temp_dist[k], chick_dist[j][k])
    if sum(temp_dist) < sum(min_dist):
        min_dist = temp_dist
    
print(sum(min_dist))

'''
