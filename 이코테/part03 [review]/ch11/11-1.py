import numpy as np
import random

while True:
    rand_n = random.randint(2, 20)
    rand_data = np.random.randint(1, rand_n, size=rand_n).tolist()
    print(rand_n)
    print(rand_data)
    print("---------------")
    n = rand_n
    data = rand_data
    data.sort()
    print(data)
    team = 0
    count = 0

    for i in range(len(data)):
        num = data[i]

        count += 1
        if count >= num:
            team += 1
            count = 0

    print("현준:", team)

    n = rand_n
    data1 = rand_data
    data1.sort()

    result = 0  # 총 그룹의 수
    count = 0  # 현재 그룹에 포함된 모험가의 수

    for i in data1:  # 공포도를 낮은 것부터 하나씩 확인하며
        count += 1  # 현재 그룹에 해당 모험가를 포함시키기
        if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1  # 총 그룹의 수 증가시키기
            count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

    print("동빈:", result)  # 총 그룹의 수 출력
    print("============")
    print()
    if team != result:
        break
