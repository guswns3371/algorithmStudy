def check_if_its_right(u):
    left = []
    for i in range(len(u)):
        if u[i] == "(":
            left.append(i)
        else:
            # left의 오른쪽 끝 원소를 꺼낸다
            if left:
                left.pop()
            else:
                return False
    return True


def divide_uv(w):
    # (
    l_gwal = 0
    # )
    r_gwal = 0
    index = -1
    for i in range(len(w)):
        # w의 왼쪽끝 원소를 꺼낸다
        now = w[i]
        if now == "(":
            l_gwal += 1
        elif now == ")":
            r_gwal += 1
        # u가 균형잡힌 괄호 문자열이 되고, 더이상 분리할 수 없는 경우
        if l_gwal == r_gwal:
            index = i
            break

    u = w[:index + 1]
    v = w[index + 1:]
    return u, v


def solution(p):
    answer = ''
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p or check_if_its_right(p):
        return p

    u, v = divide_uv(p)
    # u가 "올바른 괄호 문자열"인 경우, v에 대해 1단계부터 다시 수행
    if check_if_its_right(u):
        return u + solution(v)
    # u가 "올바른 괄호 문자열"이 아니라면
    else:
        empty_list = "(" + solution(v) + ")"
        new_u = u[1:-1]
        for i in range(len(new_u)):
            if new_u[i] == "(":
                empty_list += ")"
            else:
                empty_list += "("
        return empty_list


p = input()
print(solution(p))
