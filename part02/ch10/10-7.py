def find_team(team, x):
    if team[x] != x:
        return find_team(team, team[x])
    return team[x]


def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b


n, m = map(int, input().split())
team = [0] * (n + 1)

for i in range(1, n + 1):
    team[i] = i

for _ in range(m):
    i, a, b = map(int, input().split())
    if i == 0:
        union_team(team, a, b)
    elif i == 1:
        if find_team(team, a) == find_team(team, b):
            print('NO')
        else:
            print('YES')