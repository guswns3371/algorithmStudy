import copy


def draw(data):
    for D_LINE in data:
        for d in D_LINE:
            if d == 1:
                print("●", end=" ")
            else:
                print("○", end=" ")
        print()
    print()


def key_lock(key, lock):
    print("key", key)
    print("lock", lock)
    data_print = copy.deepcopy(lock)
    for i in range(N):
        for j in range(N):
            data_print[i][j] += key[i][j]
    print("result", data_print)


def check(key, lock):
    for i in range(N):
        for j in range(N):
            if key[i][j] == 0:
                key[i][j] = 1
            else:
                key[i][j] = 0

    if key == lock:
        return True
    else:
        return False


def rotate90(data):
    data_return = [[] for i in range(N)]

    for i in reversed(range(N)):
        for j in range(N):
            data_return[j].append(data[i][j])

    return data_return


def rotate(data, degree):
    data_return = copy.deepcopy(data)

    for _ in range(degree // 90):
        data_return = rotate90(data_return)

    return data_return


def move(data, direction):
    data_return = copy.deepcopy(data)

    if direction == _up:
        data_return.pop(0)
        data_return.append([0 for i in range(N)])
    elif direction == _down:
        data_return.insert(0, [0 for i in range(N)])
        data_return.pop(N)
    elif direction == _left:
        for D_LINE in data_return:
            D_LINE.pop(0)
            D_LINE.append(0)
    elif direction == _right:
        for D_LINE in data_return:
            D_LINE.pop(len(D_LINE) - 1)
            D_LINE.insert(0, 0)

    return data_return


def solution(key, lock):
    answer = True

    key = rotate(key, 90)
    draw(key)
    key_lock(key, lock)

    key = move(key, _right)
    draw(key)
    key_lock(key, lock)

    key = move(key, _down)
    draw(key)
    key_lock(key, lock)
    answer = check(key, lock)
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
M = len(key)
N = len(lock)
_up = 0
_down = 1
_left = 2
_right = 3

print("key")
draw(key)
print("lock")
draw(lock)
key_lock(key, lock)
print("------------------------------------------------------------")

# for i in range(1, 5):
#     print(90 * i)
#     key1 = rotate(key, 90 * i)
#     draw(key1)
#     key_lock(key1, lock)
# print("-------------")
# for i in range(4):
#     key2 = move(key, i)
#     draw(key2)
#     key_lock(key2, lock)

print("------------------------------------------------------------")

print(solution(key, lock))
