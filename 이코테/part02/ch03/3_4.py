
n, k = map(int, input().split())

count = 0
while n > k:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n -= 1
        count += 1

count += n-1
print(count)


'''
모범답안 보기 전
    n, k = map(int, input().split())
    
    count = 0
    while n != 1:
        if n % k == 0:
            n = n // k
            count += 1
        else:
            n -= 1
            count += 1
    print(count)
'''
