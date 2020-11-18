h = int(input())
m, s = 59, 59
count = 0

while True:
    if str(h).__contains__('3') or str(m).__contains__('3') or str(s).__contains__('3'):
        count += 1
    if s == 0:
        s = 59
        if m != 0:
            m -= 1
        else:
            m = 59
            if h != 0:
                h -= 1
            else:
                break
    else:
        s -= 1

print(count)

'''
if '3' in str(h) + str(m) + str(s)
'''