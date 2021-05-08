n = int(input())
army = list(map(int, input().split()))
array = [i for i in range(n)]
dp = [-1 for _ in range(n)]

for i in reversed(range(n)):
    combat = army[i]  # 현재 방문한 병사의 전투력
    behind_solider = array[i + 1:]  # 현재 방문한 병사보다 뒤에 있는 병사들의 인덱스
    max_idx = -1  # 현재 방문한 병사보다 전투력이 낮은 병사들중 가장 높은 전투력을 가진 병사의 인덱스
    max_dp = -1  # army[max_idx]
    print(f"현재 방문 : {i}번 병사(전투력:{combat}),")
    for j in behind_solider:
        if combat > army[j]:  # 현재 방문한 병사보다 전투력이 작은 병사들 중
            if max_dp < dp[j]:  # dp 값이 높은 병사의
                max_dp = dp[j]  # 전투력을 max_combat 에 담고
                max_idx = j  # 인덱스를 max_idx에 담는다

    print(f"조건에 맞는 병사 : {max_idx}")
    if max_idx == -1:  # 조건에 맞는 병사가 없다면
        dp[i] = 1
    else:
        dp[i] = dp[max_idx] + 1

    print("dp table", dp)
    print("=======================================")

print("결과", dp)
print(n - max(dp))
