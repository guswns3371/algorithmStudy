def solution1(s):
    if len(s) == 1:
        return 1

    answer = 1001
    s_index = [i for i in range(len(s))]

    # 자르는 단위의 범위 [1:문자열 길이의 절반]
    for i in range(1, (len(s) // 2) + 1):
        slicing = []
        for j in s_index[::i]:
            slicing.append(s[j:j + i])

        result = []
        num = 0
        string = slicing[0]

        for k in range(len(slicing) + 1):
            if k >= len(slicing):
                if num > 1:
                    result.append(str(num) + string)
                else:
                    result.append(string)
                break

            if string == slicing[k]:
                num += 1
            else:
                if num > 1:
                    result.append(str(num) + string)
                else:
                    result.append(string)
                num = 1
                string = slicing[k]

        if len("".join(result)) < answer:
            answer = len("".join(result))

    return answer


def compress(text, tok_len):
    words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])


print(solution("a"))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
