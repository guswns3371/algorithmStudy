n = int(input())
data = list(map(int, input()))
data.sort()
total = sum(data)
answer = 1

for d in data:

    if answer < d:
        break
    answer += d

print(answer)
