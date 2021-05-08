import numpy as np
import random

while True:
    rand_n = random.randint(2, 30)
    rand_m = random.randint(2, 10)
    rand_data = np.random.randint(1, rand_m, size=rand_n).tolist()

    print(rand_n,rand_m)
    print(rand_data)
    print("---------")
    n, m = rand_n, rand_m
    data = rand_data
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] != data[j]:
                count += 1

    print("현준:", count)

    data1 = rand_data

    # 1부터 10까지의 무게를 담을 수 있는 리스트
    array = [0] * 11

    for x in data1:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        array[x] += 1

    result = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m + 1):
        n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        result += array[i] * n  # B가 선택하는 경우의 수와 곱해주기

    print("동빈:", result)
    if count!= result:
        break
