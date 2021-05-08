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


answer = []
while True:
    edges = []
    total = 0

    m, n = map(int, input().split())
    if m == n == 0:
        break

    for _ in range(n):
        x, y, z = (map(int, input().split()))
        edges.append((z, x, y))

    parent = [0] * (m + 1)
    for i in range(1, m + 1):
        parent[i] = i

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        else:
            # 최소 신장 트리에 담을 수 없는 경우
            total += cost

    answer.append(total)


for a in answer:
    print(a)
