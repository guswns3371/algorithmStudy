data = list(input())
str_data = ""
num_data = 0
data.sort()

for d in data:
    if d.isalpha():
        str_data += d
    else:
        num_data += int(d)

print(str_data + str(num_data))
