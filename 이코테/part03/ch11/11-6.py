import heapq


def solution(food_times, k):
    q = []
    count = -1

    for i in range(len(food_times)):
        heapq.heappush(q, (i, food_times[i]))

    print('k', 'count', 'food_times', 'q')
    print(k, "*", food_times, q)
    print("---------------------")

    while q:
        idx, time = heapq.heappop(q)
        count += 1
        time -= 1

        if time != 0:
            heapq.heappush(q, (idx, time))

        print(k, count, food_times, q)

        if count == k:
            return idx + 1
        elif len(q) == 0:
            return -1
    return -1


result = solution([3, 1, 2], 4)
print(result)
