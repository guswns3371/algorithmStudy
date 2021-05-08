from collections import deque

answer = []
for _ in range(int(input())):
    only = True
    cycle = False
    result = ""

    n = int(input())
    last_year = list(map(int, input().split()))

    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(n):
        in_degree[last_year[i]] = i
        graph[last_year[i]] = last_year[i + 1:]

    graph[last_year[-1]] = []

    for _ in range(int(input())):
        a, b = map(int, input().split())

        if a in graph[b]:  # 작년에 b->a
            graph[b].remove(a)
            graph[a].append(b)
            in_degree[b] += 1
            in_degree[a] -= 1
        else: # 작년에 b->a가 아닌 경우
            graph[a].remove(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] -= 1

    q = deque()

    for i in range(n):
        if in_degree[last_year[i]] == 0:
            q.append(last_year[i])

    for i in range(n):
        if len(q) >= 2:
            only = False
            break

        if len(q) == 0:
            cycle = True
            break

        now = q.popleft()
        result += f"{now} "

        for g in graph[now]:
            in_degree[g] -= 1

            if in_degree[g] == 0:
                q.append(g)

    if not only:
        answer.append("?")
    elif cycle:
        answer.append("IMPOSSIBLE")
    else:
        answer.append(result)

for a in answer:
    print(a)
