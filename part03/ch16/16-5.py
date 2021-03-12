n_list = []

while True:
    nn = int(input())
    if nn ==0:
        break
    else:
        n_list.append(nn)

# n = int(input())

for n in n_list:
    ugly = []
    for i in range(5):  # 1,2,3,4,5 를 못생긴 수에 넣는다.
        ugly.append(i + 1)
    for i in range(n * 3):
        n2 = ugly[i] * 2
        n3 = ugly[i] * 3
        n5 = ugly[i] * 5

        if n2 not in ugly:
            ugly.append(n2)
        if n3 not in ugly:
            ugly.append(n3)
        if n5 not in ugly:
            ugly.append(n5)

    ugly.sort()
    print(ugly[n - 1])
