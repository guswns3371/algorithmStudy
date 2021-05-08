data = input()
result = int(data[0])
for i in data[1:]:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)
print(result)
