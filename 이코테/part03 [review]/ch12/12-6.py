def check(result):
    for one in result:
        x, y, a = one

        if a == 0:  # 기둥
            # 바닥 위에 있는지, 보의 한쪽 위에 있는지, 다른 기둥 위에 있는지
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result \
                    or [x, y, 1] in result:
                continue
            return False
        elif a == 1:  # 보
            # 한쪽 부분이 기둥 위에 있는지, 양쪽 끝 부분이 다른 보와 연결되었는지
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result \
                    or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            return False

    return True


def solution(n, build_frame):
    result = []
    for build in build_frame:
        x, y, a, b = build

        # 일단 result에 반영
        if b == 0:  # 삭제
            if [x, y, a] in result:
                result.remove([x, y, a])
        elif b == 1:  # 설치
            if [x, y, a] not in result:
                result.append([x, y, a])

        # 가능한 건축인지 확인
        if not check(result):
            # rollback
            if b == 0:
                if [x, y, a] not in result:
                    result.append([x, y, a])
            elif b == 1:
                if [x, y, a] in result:
                    result.remove([x, y, a])
    result.sort()
    return result


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
               [3, 2, 1, 1]]
print(solution(n, build_frame))

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame))
