def gprint(data):
    for dd in data:
        for d in dd:
            print(d, end=" ")
        print()


def rotate_key(key):
    m = len(key)
    cp_key = [[0 for _ in range(m)] for _ in range(m)]

    for i in reversed(range(m)):
        for j in range(m):
            cp_key[j][m - 1 - i] = key[i][j]

    return cp_key


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 확장된 lock
    ext_lock = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            ext_lock[i + n][j + n] = lock[i][j]

    for i in range(1, 2 * n):
        for j in range(1, 2 * n):

            for k in range(4):
                check = False

                # lock에 key를 더함
                for a in range(m):
                    for b in range(m):
                        ext_lock[i + a][j + b] += key[a][b]

                # key 가 lock에 맞는지 확인
                for a in range(n):
                    if 0 in ext_lock[n:2 * n][a][n:2 * n] or 2 in ext_lock[n:2 * n][a][n:2 * n]:
                        check = True
                        break

                if check:
                    # lock에 key를 뺌
                    for a in range(m):
                        for b in range(m):
                            ext_lock[i + a][j + b] -= key[a][b]
                else:
                    # lock에 key가 맞음!
                    return True

                # key 회전
                key = rotate_key(key)

            # key 회전
            key = rotate_key(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
