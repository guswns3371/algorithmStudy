s_list = list(map(int, input()))
# 연속된 0의 개수
zero_cnt = 0
# 연속된 1의 개수
one_cnt = 0

# 연속된 0,1의 개수를 구하기위한 플래그 변수
zero_flag = True
one_flag = True

for i in s_list:
    if i == 0 and zero_flag:
        # zero_flag = False 를 통해 최초의 0을 만날때만 카운트
        zero_flag = False
        zero_cnt += 1
        # 1이 나올 떄 카운트하기 위해 필요한 부분.
        one_flag = True

    if i == 1 and one_flag:
        # zero_flag = False 를 통해 최초의 1을 만날때만 카운트
        one_flag = False
        one_cnt += 1
        zero_flag = True

if zero_cnt + one_cnt == 1:
    # 00..0 또는 11..1 인 경우
    print(1)
elif zero_cnt == one_cnt:
    # 연속된 0의 개수와 연속된 1의 개수가 같은 경우
    print(zero_cnt)
elif zero_cnt != one_cnt:
    # 연속된 0의 개수와 연속된 1의 개수중 최소횟수 출력
    print(min(zero_cnt, one_cnt))
