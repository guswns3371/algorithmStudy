import string
import random

# 테스트 케이스 만들기
result = ""
_LENGTH = 15
n = random.randint(1, 100)
string_pool = string.ascii_uppercase + string.digits
for i in range(_LENGTH):  # 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다.
    result += random.choice(string_pool)
print("입력:", result)

input_list = result
number_list = []
string_list = []

for i in range(len(input_list)):
    try:
        num = int(input_list[i])
        number_list.append(num)
    except ValueError:
        string_list.append(input_list[i])

string_list.sort()
for s in string_list:
    print(s, end="")
print(sum(number_list))

# print(string_list)
# print(number_list)
