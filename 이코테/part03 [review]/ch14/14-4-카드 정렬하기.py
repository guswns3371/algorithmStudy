# [카드 정렬하기](https://www.acmicpc.net/problem/1715)
import heapq

answer = 0
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
heapq.heapify(data)

while len(data) > 1:
    a, b = heapq.heappop(data), heapq.heappop(data)
    answer += a + b
    heapq.heappush(data, a + b)

print(answer)
