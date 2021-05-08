from bisect import bisect_left, bisect_right


def count_by_range(arr, left, right):
    return bisect_right(arr, right) - bisect_left(arr, left)


def solution(words, queries):
    answer = [0] * len(queries)

    for i in range(len(words)):
        len_w = len(words[i])
        array[len_w].append(words[i])
        reversed_array[len_w].append(words[i][::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for i in range(len(queries)):
        query = queries[i]
        len_q = len(query)

        if query[0] == "?":  # 접두사가 와일드 카드인 경우 : ??___
            query = query[::-1]  # ___?? 형태로 뒤집는다
            n_array = reversed_array[len_q]  # 뒤집어진 단어 리스트를 담는 리스트를 가져온다
        else:  # 접미사가 와일드 카드인 경우 : ___??
            n_array = array[len_q]  # 정상적인 단어 리스트를 담는 리스트를 가져온다

        left = query.replace("?", "a")  # ___aa
        right = query.replace("?", "z")  # ___zz
        answer[i] = count_by_range(n_array, left, right)

    return answer


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
