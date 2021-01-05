def turn_left(pd):
    if pd == 0:
        return 3
    else:
        return pd - 1


def go(pd, pa, pb):
    if pd == 0:
        pb -= 1
    elif pd == 1:
        pa += 1
    elif pd == 2:
        pb += 1
    else:
        pa -= 1
    return pa, pb


def back(pd, pa, pb):
    if pd == 0:
        pb += 1
    elif pd == 1:
        pa -= 1
    elif pd == 2:
        pb -= 1
    else:
        pa += 1
    return pa, pb


n, m = map(int, input().split())
a, b, d = map(int, input().split())
been_there = [[a, b]]
game_map = []
ori_d = d

for i in range(n):
    game_map.append(list(map(int, input().split())))

while True:
    alert = 0
    for i in range(4):
        d = turn_left(d)
        a, b = go(d, a, b)
        if game_map[a][b] == 1 or [a, b] in been_there:
            alert += 1
            a, b = back(d, a, b)
            continue
        been_there.append([a, b])

    if alert == 4:
        d = ori_d
        a, b = back(d, a, b)
        if game_map[a][b] == 1:
            break

print(been_there)

"""
4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

3 3
1 1 0
1 1 1
1 0 0
1 1 0

5 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 0 0 1
1 1 1 1

[의사 코드]
ori_d = d

while True:
    alert =0
    for i in range(4):
        turn_left() # d값이 변한다
        go()
        if 바다 or 가본적있는 지점:
            alert +=1
            back()
            continue
        been_there 에 추가
    
    if alert ==4 :
        d = ori_d
        back()
        if 바다 :
            break
"""
