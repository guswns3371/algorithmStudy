from collections import deque

answer = []
for _ in range(int(input())):
    idk = False
    impossible = False
    result = ""

    n = int(input())
    last_year = list(map(int, input().split()))
    two_teams = []

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    # 각 노드에 대한 진입차수 삽입, 연결된 노드 리스트 삽입
    for i in range(1, n + 1):
        temp = last_year[i - 1:]
        temp.pop(0)

        graph[last_year[i - 1]] = temp
        in_degree[last_year[i - 1]] = i-1

    # 등수가 바뀐 팀의 쌍 입력받기
    for _ in range(int(input())):
        two_teams.append(list(map(int, input().split())))

    # 바뀐 등수 적용하기
    for two_team in two_teams:
        a, b = two_team
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)

            in_degree[a] -= 1
            in_degree[b] += 1
        else:
            impossible = True
            break

    if impossible:
        answer.append("IMPOSSIBLE")
        continue

    # 위상 정렬
    q = deque()
    for i in range(n):
        if in_degree[last_year[i]] == 0:
            q.append(last_year[i])
            break

    while q:
        if len(q) >= 2:
            idk = True
            break

        if len(q) == 0:
            impossible = True
            break

        now = q.popleft()
        result += f"{now} "

        for g in graph[now]:
            in_degree[g] -= 1
            if in_degree[g] == 0:
                q.append(g)

    if impossible:
        answer.append("IMPOSSIBLE")
        continue
    elif idk:
        answer.append("?")
        continue
    else:
        answer.append(result)

for a in answer:
    print(a)
