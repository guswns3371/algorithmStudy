# [실패율](https://programmers.co.kr/learn/courses/30/lessons/42889)
def solution(N, stages):
    failure = []
    p_count = len(stages)
    for i in range(N):
        s_count = stages.count(i + 1)
        if p_count <= 0:
            failure.append((i + 1, 0))
            continue
        failure.append((i + 1, s_count / p_count))
        p_count -= s_count

    failure = sorted(failure, key=lambda x: (-x[1], x[0]))
    return [f[0] for f in failure]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
