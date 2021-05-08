import numpy as np
import random
import copy

random_t = random.randint(1, 1000)

keep_going = True
while keep_going:
    random_n = random.randint(1, 20)
    random_m = random.randint(1, 20)
    random_array = np.random.randint(1, 101, (1, random_n * random_m))[0]

    print("<input>")
    print("n=", random_n, "m=", random_m)

    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    answer = []

    # t = int(input())

    # for _ in range(t):
    n, m = random_n, random_m
    lst = random_array

    d = []
    graph = []
    result = []

    for i in range(n):
        graph.append(lst[m * i:m * i + m])

    d = copy.deepcopy(graph)

    # # 메모이제이션
    # for i in range(n):
    #     d[i][m - 1] = graph[i][m - 1]

    for y in reversed(range(m - 1)):
        for x in range(n):
            max_num = -int(1e9)
            for j in range(3):
                nx = x + dx[j]
                ny = y + dy[j]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if max_num < d[nx][ny]:
                    max_num = d[nx][ny]

            d[x][y] = d[x][y] + max_num

    print("graph")
    for i in graph:
        for ii in i:
            print(ii, end=" ")
        print()

    print("------------------")
    print("dp table")
    for i in d:
        for ii in i:
            print(ii, end=" ")
        print()

    result = -int(1e9)
    for i in range(n):
        if result < d[i][0]:
            result = d[i][0]

    print("=================")
    print("현준답안:", result)

    # 모범답안
    # 금광 정보 입력
    n, m = random_n, random_m
    array = random_array

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result2 = []
    for i in range(n):
        result2.append(dp[i][m - 1])

    print("모범답안:", max(result2))

    if result != max(result2):
        keep_going = False
    print("🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐")
