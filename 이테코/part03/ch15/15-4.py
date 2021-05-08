def check(word, query):
    if len(word) == len(query):
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

"""
class Node(object):
    def __init__(self, key, count=0):
        self.key = key  # 해당 문자를 key값으로 가진다.
        self.child = {}  # 자식노드들을 Dict에 저장을 한다.


class Trie(object):
    def __init__(self):
        self.head = Node(None)  # 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.

    def insert(self, word):
        cur = self.head  # 빈 노드인 head를 cur에 할당한다.

        for ch in word:  # word 문자열의 각 문자 ch에 대해
            if ch not in cur.child:
                # 해당 문자 ch가 현재 방문 노드 cur의 자식노드(dict)에 존재하지 않을 경우
                # cur의 자식노드에 ch를 key로 갖는 노드 Node(ch)를 추가한다.
                cur.child[ch] = Node(ch)

            cur = cur.child[ch]  # ch를 key로 갖는 노드의 자식노드를 그다음 방문한다.
        cur.child['*'] = True  # 문자열의 마지막에 '*'을 삽입.

    def search(self, word):
        cur = self.head  # 빈 노드인 head를 cur에 할당한다.

        for ch in word:  # word 문자열의 각 문자 ch에 대해
            if ch not in cur.child:
                # 해당 문자 ch가 현재 방문 노드 cur의 자식노드(dict)에 존재하지 않을 경우
                # False를 반환한다
                return False

            cur = cur.child[ch]  # ch를 key로 갖는 노드의 자식노드를 그다음 방문한다.
        if '*' in cur.child:  # 햔제 빙문노드의 자식노드가 *문자를 가지고있다면 true를 반환한다.
            return True


# test code
trie = Trie()
trie.insert('hooong')
# trie.insert('hi')
# trie.insert('how')
print(trie.search('hooong'))
# print(trie.search('hi'))
# print(trie.search('how'))
# print(trie.search('home'))
"""

