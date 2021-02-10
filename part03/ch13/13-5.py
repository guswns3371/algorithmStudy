import itertools

n = int(input())
number_list = list(map(int, input().split()))

# add, sub, mul, div
num_operator = list(map(int, input().split()))

# 각 연산자의 개수만큼 연산자를 operator_list에 담는다
operator_list = []
for o in range(4):
    for _ in range(num_operator[o]):
        operator_list.append(o)

result_list = []

# 연산자는 (n-1)P(n-1) : 연산자 n-1 개중에서 n-1개를 선택하는 경우의 수
num_of_cases = [list(p) for p in itertools.permutations(operator_list, n - 1)]

min_val = int(1e9)
max_val = -int(1e9)

first = number_list.pop(0)
for nc in num_of_cases:
    result = first
    # 규칙에 맞게 계산
    for i in range(n-1):
        if nc[i] == 0:
            result += number_list[i]
        elif nc[i] == 1:
            result -= number_list[i]
        elif nc[i] == 2:
            result *= number_list[i]
        elif nc[i] == 3:
            if result < 0:
                result = abs(result) // number_list[i]
                result = (-1) * result
            else:
                result = abs(result) // number_list[i]

    if result < min_val:
        min_val = result
    if result > max_val:
        max_val = result

print(max_val)
print(min_val)

"""
n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val, max_val = int(1e9), -int(1e9)


def dfs(i, res, add, sub, mul, div):
    global min_val, max_val
    if i == n:
        max_val = max(res, max_val)
        min_val = min(res, min_val)
        return
    else:
        if add:
            dfs(i + 1, res + nums[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, res - nums[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, res * nums[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(res / nums[i]), add, sub, mul, div - 1)


dfs(1, nums[0], add, sub, mul, div)
print(max_val)
print(min_val)
"""

"""
import itertools

n = int(input())
algebra = [-1] * (2 * n)
num_list = list(map(int, input().split()))

# algebra 리스트의 인덱스가 짝수인 칸에 숫자를 넣는다
for i in range(n):
    algebra[2 * i] = num_list[i]

# add, sub, mul, div
num_operator = list(map(int, input().split()))
operator_list = []
for o in range(4):
    tmp_list = [o for _ in range(num_operator[o])]
    operator_list = list(itertools.chain(operator_list, tmp_list))

print("algebra", algebra)
print("operator_list", operator_list)
result_list = []

# 연산자는 (n-1)P(n-1) : 연산자 n-1 개중에서 n-1개를 선택하는 경우의 수
num_of_cases = [list(p) for p in itertools.permutations(operator_list, n - 1)]

print("num_of_cases")
a = 0
for nc in num_of_cases:
    a += 1
    print(a, "번", end=" algebra : ")

    # algebra 리스트의 인덱스가 홀수인 칸에 연산자를 넣는다, 마지막 인덱스는 빈칸으로 남긴다.
    for i in range(n - 1):
        algebra[2 * i + 1] = nc[i]

    # 수식 출력
    str_algebra = ""
    for i in range(len(algebra)):
        # 인덱스가 짝수인 원소 : 숫자, 인덱스가 홀수인 원소 : 연산자
        if i % 2 == 0:
            str_algebra += str(algebra[i])
        else:
            if algebra[i] == 0:
                str_algebra += "+"
            elif algebra[i] == 1:
                str_algebra += "-"
            elif algebra[i] == 2:
                str_algebra += "*"
            elif algebra[i] == 3:
                str_algebra += "/"
    print(str_algebra)
    print(algebra)
    # 규칙에 맞게 계산

    result = algebra[0]
    for i in range(1, 2 * n, 2):
        print(result, end=" ")
        # tmp_list 형식 : [연산자,숫자]
        tmp_list = algebra[i:i + 2]
        if tmp_list[0] == 0:
            result += tmp_list[1]
            print("+", tmp_list[1], end="=")
        elif tmp_list[0] == 1:
            result -= tmp_list[1]
            print("-", tmp_list[1], end="=")
        elif tmp_list[0] == 2:
            result *= tmp_list[1]
            print("*", tmp_list[1], end="=")
        elif tmp_list[0] == 3:
            if result < 0:
                result = abs(result) // tmp_list[1]
                result = (-1) * result
            else:
                result = abs(result) // tmp_list[1]
            print("/", tmp_list[1], end="=")
        elif tmp_list[0] == -1:
            break

        print(result, end=" --> ")
    print()
    result_list.append(result)

print(max(result_list))
print(min(result_list))
"""
