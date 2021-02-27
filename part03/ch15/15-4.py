from bisect import bisect_right


def check(word, query):
    if len(word) == len(query):
        # list_q.sort()
        # wild_length = bisect_right(list_q, "?")
        wild_length = query.count("?")
        if query[0] == "?":
            if query[wild_length:] == word[wild_length:]:
                return True
        else:
            if query[:-wild_length] == word[:-wild_length]:
                return True

    return False


def solution(words, queries):
    len_q = len(queries)
    answer = [0] * len_q
    for i in range(len_q):
        for j in range(len(words)):
            if check(words[j], queries[i]):
                answer[i] += 1

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
