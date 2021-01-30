import copy


def draw(data):
    for d_line in data:
        for d in d_line:
            if d == 1:
                print("●", end=" ")
            else:
                print("○", end=" ")
        print()
    print()


def check(key, lock):
    n = len(lock)
    total = 0
    for i in range(n):
        for j in range(n):
            if key[i][j] + lock[i][j] == 1:
                total += key[i][j] + lock[i][j]
            else:
                return False
    if total == n * n:
        return True
    else:
        return False


def rotate90(key):
    m = len(key)
    ret = [[] for _ in range(m)]

    for i in reversed(range(m)):
        for j in range(m):
            ret[j].append(key[i][j])

    return ret


def rotate(key, degree):
    ret = copy.deepcopy(key)

    for _ in range(degree // 90):
        ret = rotate90(ret)

    return ret


def move(key, direction):
    m = len(key)
    ret = copy.deepcopy(key)

    if direction == _up:
        ret.pop(0)
        ret.append([0 for _ in range(m)])
    elif direction == _down:
        ret.insert(0, [0 for _ in range(m)])
        ret.pop(m)
    elif direction == _left:
        for r_line in ret:
            r_line.pop(0)
            r_line.append(0)
    elif direction == _right:
        for r_line in ret:
            r_line.pop(len(r_line) - 1)
            r_line.insert(0, 0)

    return ret


def direction_translate(direction):
    if direction == _up:
        return "up"
    elif direction == _down:
        return "down"
    elif direction == _left:
        return "left"
    elif direction == _right:
        return "right"


def simulate(key, degree, direction, lock):
    global answer
    answer = False
    m = len(key)
    ret_key = copy.deepcopy(key)
    print(f"<key> : {90 * degree}도 -> {direction_translate(direction)}이동")
    draw(ret_key)

    # 옮겨진 key가 모두 0이 될 경우
    tot = 0
    for i in range(m):
        for j in range(m):
            tot += ret_key[i][j]

    if tot == 0:
        answer = False
        draw(ret_key)
        print("------------------------------------------------False : key 가 모두 0")

    ret_key = rotate(ret_key, 90 * degree)
    print(f"{90 * degree}도 회전")
    draw(ret_key)

    if check(ret_key, lock):
        answer = True
        print(f"------------------------------------------------True : {90 * degree}도 회전")
        return True
    else:
        print(f"------------------------------------------------False : {90 * degree}도 회전")

    ret_key = move(ret_key, direction)
    print(f"{direction_translate(direction)}으로 이동")
    draw(ret_key)

    if check(ret_key, lock):
        answer = True
        print(f"------------------------------------------------True : {direction_translate(direction)}으로 이동")
        return True
    else:
        print(f"------------------------------------------------False : {direction_translate(direction)}으로 이동")

    degree += 1
    direction += 1
    for deg in range(degree, 4):
        for direct in range(direction, 4):
            simulate(key, deg, direct, lock)

    print(f"------------------------------------------------{answer} : 마지막")
    return answer


def solution(key, lock):
    m = len(key)
    n = len(lock)
    # key 의 크기를 m x m => n x n으로 변환 (빈 공간은 0으로 채운다)
    new_key = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[i][j]

    draw(lock)
    return simulate(new_key, 0, 0, lock)


_up = 0
_down = 1
_left = 2
_right = 3

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
