lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
s = input()

col = lst.index(s[0]) + 1
row = int(s[1])

dx = [-2, 2]
dy = [-1, 1]
count = 0

for x in dx:
    for y in dy:
        if col + x < 1 or col + x > 8 or row + y < 1 or row + y > 8:
            count += 0
        else:
            #  (-2,-1) (-2,1) (2,-1) (2,1) 를 더할 경우
            count += 1
            if col + y < 1 or col + y > 8 or row + x < 1 or row + x > 8:
                count += 0
            else:
                #  (-1,-2) (1,-2) (-1,2) (1,2) 를 더할 경우
                count += 1

print(count)
