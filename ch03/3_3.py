
n, m = map(int, input().split())
# 내 풀이
result = -1

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()

    if result == -1:
        result = data[0]
    else:
        if result <= data[0]:
            result = data[0]

print('result : ', result)

'''
4 3
2 2 5
5 3 3
2 2 2
7 1 5
'''