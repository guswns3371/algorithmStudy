s_list = list(map(int, input()))
# 첫번쨰
result = s_list[0]

for i in range(1, len(s_list)):
    if s_list[i] == 0 or s_list[i] == 1 or result == 0 or result == 1:
        result += s_list[i]
    else:
        result *= s_list[i]

print(result)
