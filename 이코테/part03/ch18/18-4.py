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


def calculate_cost(A, B):
    return min(abs(A[0] - B[0]), abs(A[1] - B[1]), abs(A[2] - B[2]))


n = int(input())
nodes = []
edges = []
total_cost = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((calculate_cost(nodes[i], nodes[j]), i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
