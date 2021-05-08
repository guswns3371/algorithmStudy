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


# 입력 받는 부분
n, m = map(int, input().split())
graph = []
parent = [0] * (n + 1)
group = [[] for _ in range(n)]

for i in range(1, n + 1):
    parent[i] = i

for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = map(int, input().split())
possible = None

# 입력받은 graph 를 기반으로 union 연산을 수행한다.
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            union_parent(parent, a + 1, b + 1)

# graph[부모노드 번호] = [자식노드들 ..] 이 되도록 append한다.
for i in range(1, n + 1):
    group[parent[i]].append(i)

for sub_group in group:
    possible = True
    for p in plan:
        if p not in sub_group:
            # 여행 계획의 여행지들이 하나의 sub_group에 속하지 않으면 여행계획이 불가능하다.
            possible = False

    if possible:
        break

if possible:
    print("YES")
else:
    print("NO")
"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
