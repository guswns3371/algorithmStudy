n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
result = 0
a_list = sorted(a_list, reverse=False)
b_list = sorted(b_list, reverse=True)

for i in range(k):
    if a_list[i] < b_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
    else:
        break

for i in a_list:
    result += i
print(result)

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
