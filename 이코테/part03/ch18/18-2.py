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


g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]
p_gate = []
total = 0
for _ in range(p):
    p_gate.append(int(input()))

for i in range(p):
    root = find_parent(parent, p_gate[i]) # i번 비행기의 gi에 해당하는 게이트의 부모노드
    if root != 0:
        union_parent(parent, root, root - 1)
        total += 1
    else:
        break

print(total)
