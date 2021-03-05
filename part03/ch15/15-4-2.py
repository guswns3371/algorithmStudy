# class Node(object):
#     def __init__(self, key, count=0):
#         self.key = key  # 해당 문자를 key값으로 가진다.
#         self.child = {}  # 자식노드들을 Dict에 저장을 한다.
#
#
# class Trie(object):
#     count = 0
#
#     def init_count(self):
#         Trie.count = 0
#
#     def get_count(self):
#         return Trie.count
#
#     def __init__(self):
#         self.head = Node(None)  # 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.
#
#     def insert(self, word):
#         cur = self.head  # 빈 노드인 head를 cur에 할당한다.
#
#         for ch in word:  # word 문자열의 각 문자 ch에 대해
#             if ch not in cur.child:
#                 # 해당 문자 ch가 현재 방문 노드 cur의 자식노드(dict)에 존재하지 않을 경우
#                 # cur의 자식노드에 ch를 key로 갖는 노드 Node(ch)를 추가한다.
#                 cur.child[ch] = Node(ch)
#
#             cur = cur.child[ch]  # ch를 key로 갖는 노드의 자식노드를 그다음 방문한다.
#         cur.child['*'] = True  # 문자열의 마지막에 '*'을 삽입.
#
#     def search(self, word):
#         cur = self.head  # 빈 노드인 head를 cur에 할당한다.
#
#         for i in range(len(word)):  # word 문자열의 각 문자 ch에 대해
#             ch = word[i]
#             if ch == "?":
#                 for key, value in cur.child.items():
#                     cnt = i
#                     now = value.child
#
#                     print(value.key, value.child)
#             if ch not in cur.child:
#                 # 해당 문자 ch가 현재 방문 노드 cur의 자식노드(dict)에 존재하지 않을 경우
#                 # False를 반환한다
#                 return False
#
#             cur = cur.child[ch]  # ch를 key로 갖는 노드의 자식노드를 그다음 방문한다.
#         if '*' in cur.child:  # 햔제 빙문노드의 자식노드가 *문자를 가지고있다면 true를 반환한다.
#             return True
#
#
# def solution(words, queries):
#     len_q = len(queries)
#     answer = [0] * len_q
#     trie = Trie()
#     for w in words:
#         trie.insert(w)
#
#     for i in range(len_q):
#         print("💎", queries[i], "💎")
#         trie.search(queries[i])
#         answer[i] = trie.get_count()
#         print(answer[i], "💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎")
#         trie.init_count()
#
#     return answer
#
#
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
#
# print(solution(words, queries))

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string

    # 문자열이 존재하는지 search
    def search(self, string):
        # 가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        # 탐색이 끝난 후 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다.
        if curr_node.data is not None:
            return True
