"""
네트워크 https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    data = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                data[i].append(j)
    for i in range(n):
        if visited[i] == 1:
            continue
        q = deque([i])
        visited[i] = 1
        answer += 1
        while q:
            now = q.popleft()
            for node in data[now]:
                if visited[node] != 1:
                    visited[node] = 1
                    q.append(node)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
