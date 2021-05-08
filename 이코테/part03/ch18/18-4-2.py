def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

for i in range(n):
    dx, dy, dz = map(int, input().split())
    x.append([dx, i])
    y.append([dy, i])
    z.append([dz, i])

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    # (행성i,i+1의 x축 사이의 거리, 행성번호 i, 행성번호 i+1) -> y,z축에 대해서도 똑같이 한다
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# x,y,z축에서 각각 구한 행성간의 거리를 기준으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
