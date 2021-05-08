data = list(map(int, input()))
one_flag = True
zero_flag = True
one = 0
zero = 0

if len(data) == 1:
    print(0)
else:
    for i in range(len(data)):
        num = data[i]

        if num == 0 and zero_flag:
            zero += 1
            zero_flag = False
            one_flag = True
        if num == 1 and one_flag:
            one += 1
            one_flag = False
            zero_flag = True
    if zero + one == 1:
        print(0)
    else:
        print(min(zero, one))