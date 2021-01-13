def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
# 간선 배열
edges = [] * (m + 1)

# 신장 트리
parent = [0] * (n + 1)

# 자기 자신을 부모노드로 설정
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    # 비용 c를 기준으로 정렬하기 위해 c를 첫번쟤에 둔다
    edges.append((c, a, b))

# 비용이 작은 순서대로 m개의 길을 정렬
edges.sort()
result = 0
maximum = 0
for edge in edges:
    c, a, b = edge

    # a와 b가 신장트리에 포함되어있는지 확인 = 동일 집합에 포함되는지 확인 = 부모노드가 같은지 확인
    if find_parent(parent, a) != find_parent(parent, b):
        # a-b 경로를 신장트리에 포함하는 과정
        union_parent(parent, a, b)
        result += c
        if c > maximum:
            maximum = c

print(result - maximum)
