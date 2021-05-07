from itertools import permutations
from bisect import bisect_right


def solution(n, weak, dist):
    check = len(weak)
    perms = list(permutations(dist))
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    result = []

    for perm in perms:
        for start in range(len(weak) // 2):
            fcheck = 0
            count = 0
            for friend in perm:
                count += 1

                end = bisect_right(weak, weak[start] + friend)
                fcheck += end - start

                start = end

                if fcheck >= check:
                    result.append(count)
                    break

    if len(result) == 0:
        return -1

    return min(result)


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
