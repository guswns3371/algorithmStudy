# [가사 검색](https://programmers.co.kr/learn/courses/30/lessons/60060)
from bisect import bisect


def solution(words, queries):
    answer = []
    data = {}
    rdata = {}

    for word in words:
        if not data.get(len(word)):
            data[len(word)] = []
            rdata[len(word)] = []
        data[len(word)].append(word)
        rdata[len(word)].append(word[::-1])

    for key, value in data.items():
        value.sort()
    for key, value in rdata.items():
        value.sort()

    for query in queries:
        if not data.get(len(query)):
            answer.append(0)
            continue
        if query[0] != "?":
            twords = data[len(query)]
        else:
            twords = rdata[len(query)]
            query = query[::-1]

        start = query.replace("?", "a")
        end = query.replace("?", "z")
        count = bisect(twords, end) - (bisect(twords, start))
        answer.append(count)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
