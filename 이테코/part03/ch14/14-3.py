def solution(N, stages):
    count = []
    num_of_players = len(stages)
    num_of_stage = [0] * (N + 2)

    # 계수정렬
    for i in range(len(stages)):
        num_of_stage[stages[i]] += 1

    for i in range(1, N + 1):
        # 만약 도달한 사람이 없는 단계가 있을 경우 실패율을 0으로 정의함
        if num_of_players <= 0:
            count.append((0, i))
            continue
        num_of_i = num_of_stage[i]
        # 원소 형식 : (실패율, 스테이지 번호)
        count.append((num_of_i / num_of_players, i))
        print(f"{i}번 스테이지 실패율 = {num_of_i}/{num_of_players}")
        num_of_players -= num_of_i

    # 실패율을 기준으로 내림차순, 실패율이 같다면 스테이지 번호 기준으로 오름차순
    result = sorted(count, key=lambda x: [-x[0], x[1]])
    answer = [result[i][1] for i in range(N)]
    print(answer)
    return answer


solution(5, [2, 1, 2, 6, 6, 2, 4, 4, 4, 4, 3, 3])
solution(4, [3])
