import timeit
import random

keep = True
while keep:
    random_n = random.randint(1, 1000)
    print(f"🔥 n = {random_n}")

    n = random_n

    start_time = timeit.default_timer()  # 시작 시간 체크

    ugly1 = [0] * n  # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
    ugly1[0] = 1  # 첫 번째 못생긴 수는 1

    # 2배, 3배, 5배를 위한 인덱스
    i2 = i3 = i5 = 0
    # 처음에 곱셈 값을 초기화
    next2, next3, next5 = 2, 3, 5

    # 1부터 n까지의 못생긴 수들을 찾기
    for l in range(1, n):
        # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
        ugly1[l] = min(next2, next3, next5)
        # 인덱스에 따라서 곱셈 결과를 증가
        if ugly1[l] == next2:
            i2 += 1
            next2 = ugly1[i2] * 2
        if ugly1[l] == next3:
            i3 += 1
            next3 = ugly1[i3] * 3
        if ugly1[l] == next5:
            i5 += 1
            next5 = ugly1[i5] * 5

    # n번째 못생긴 수를 출력
    print(ugly1)
    print("동빈 :", ugly1[n - 1], end=" 👉 ")

    terminate_time = timeit.default_timer()  # 종료 시간 체크
    print("%f초 걸렸습니다." % (terminate_time - start_time))

    """=============================================="""
    n = random_n

    start_time = timeit.default_timer()  # 시작 시간 체크

    ugly = []
    for i in range(5):  # 1,2,3,4,5 를 못생긴 수에 넣는다.
        ugly.append(i + 1)

    for i in range(n * 3):
        n2 = ugly[i] * 2
        n3 = ugly[i] * 3
        n5 = ugly[i] * 5

        if n2 not in ugly:
            ugly.append(n2)
        if n3 not in ugly:
            ugly.append(n3)
        if n5 not in ugly:
            ugly.append(n5)

    ugly.sort()
    print(ugly)
    print("현준 :", ugly[n - 1], end=" 👉 ")
    terminate_time = timeit.default_timer()  # 종료 시간 체크
    print("%f초 걸렸습니다." % (terminate_time - start_time))
    if terminate_time - start_time >= 1.0:
        print("시간초과!!!🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")

    keep = ugly[n - 1] == ugly1[n - 1]
    print(keep)
    print("==================================================")
    print()
