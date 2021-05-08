# 모험가 수
n = int(input())
# 각 모험가의 공포도
n_list = list(map(int, input().split()))

# 내림차순으로 정렬 : 공포도가 높은 순서로 정렬
# 3 2 2 2 1
n_list = sorted(n_list, reverse=True)
print(n_list)
for i in range(n):
    print(i, n_list[len(n_list) - i + 1:])
