def check(p):
    total = 0
    if p[0] == ")":
        return False
    for i in range(len(p)):
        if p[i] == "(":
            total += 1
        elif p[i] == ")":
            total -= 1
        if total < 0:
            return False
    return True


def solution(p):
    if len(p) == 0:
        return ""

    start, end = 0, 0
    u, v = "", ""

    for i in range(len(p)):
        if p[i] == "(":
            start += 1
        elif p[i] == ")":
            end += 1

        if start == end:
            u = p[:i + 1]
            if i < len(p) - 1:
                v = p[i + 1:]
            break

    if check(u):
        return u + solution(v)

    answer = "(" + solution(v) + ")"
    for s in u[1:-1]:
        if s == "(":
            answer += ")"
        elif s == ")":
            answer += "("
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
