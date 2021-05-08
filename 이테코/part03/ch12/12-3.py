def solution(s):
    answer = int(1e9)
    # level 단위로 문자열 자르고 -> temp_list에 담기
    for level in range(1, (len(s) // 2) + 1):
        cut = []
        compression = []
        start = 0
        while True:
            cut.append(s[start:start + level])
            start += level
            if start > len(s) - 1:
                break
        print(level, "개 단위 : ", cut)

        # t_compression을 cut[0] 값으로 초기화
        t_compression = cut.pop(0)

        for i in range(len(cut)):
            now = cut[i]
            compare = ""
            count = 0
            decimal_end = -1

            for t in range(len(t_compression)):
                if t_compression[t].isdecimal():
                    decimal_end = t
                else:
                    if decimal_end == -1:
                        count = 1
                        compare = t_compression
                    else:
                        count = int(t_compression[0:decimal_end+1])
                        compare = t_compression[decimal_end+1:]

            print(compare, now, end=" ")
            if compare == now:
                count += 1
                t_compression = str(count) + compare
            else:
                compression.append(t_compression)
                t_compression = now

            if i == len(cut) - 1:
                compression.append(t_compression)

            print(t_compression)

        result = ""
        for val in compression:
            result += val
        answer = min(answer, len(result))
        print(compression, result, len(result))

    if len(s) == 1:
        answer = 1

    return answer


s = "a"
print(solution(s))
