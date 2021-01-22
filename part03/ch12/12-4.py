import copy


def print_data(data):
    for D_LINE in data:
        for d in D_LINE:
            if d == 1:
                print("●", end=" ")
            else:
                print("○", end=" ")
        print()
    print()


def check(key, lock):
    for i in range(N):
        for j in range(N):
            if key[i][j] == 0:
                key[i][j] = 1
            else:
                key[i][j] = 0

    if key == lock:
        print("true")
    else:
        print("false")


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

    if direction == "up":
        data_return.pop(0)
        data_return.append([0 for i in range(N)])
    elif direction == "down":
        data_return.insert(0, [0 for i in range(N)])
        data_return.pop(N)
    elif direction == "left":
        for D_LINE in data_return:
            D_LINE.pop(0)
            D_LINE.append(0)
    elif direction == "right":
        for D_LINE in data_return:
            D_LINE.pop(len(D_LINE) - 1)
            D_LINE.insert(0, 0)

    return data_return


def solution(key, lock):
    answer = True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
N = len(key)
M = len(lock)

solution(key, lock)
