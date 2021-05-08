n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0
count = 0

# 내 풀이
while True:
    for i in range(k):
        if count == m:
            break
        result += first
        count += 1
        print(first, end=", ")
    if count == m:
        break
    result += second
    count += 1
    print(second)

print()
print("[1] result : ", result)

# 모범답안 살짝 참고
q = m // (k + 1)
r = m % (k + 1)
result = q * (k * first + second) + r * first
print("[2] result : ", result)
