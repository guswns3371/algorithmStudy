from collections import deque
from bisect import bisect_left, insort_left


def get_x(data):
    return int(data[2])


def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    assignment = [i for i in range(n)]

    deleted = deque([])

    for one_cmd in cmd:
        if one_cmd[0] == "U":
            k -= get_x(one_cmd)
        elif one_cmd[0] == "D":
            k += get_x(one_cmd)
        elif one_cmd[0] == "C":  # 삭제
            before_len = len(assignment)

            deleted.append(assignment[k])
            assignment.remove(assignment[k])

            if k == before_len - 1:
                k -= 1

        elif one_cmd[0] == "Z":
            r_val = deleted.pop()

            r_index = bisect_left(assignment, r_val)
            insort_left(assignment, r_val)

            if r_index <= k:
                k += 1

    while deleted:
        d = deleted.pop()
        answer[d] = "X"
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
