import heapq

n = int(input())
card = []
total = 0
for _ in range(n):
    card.append(int(input()))

card.sort()
heapq.heapify(card)

if n >= 2:
    while card:
        a = heapq.heappop(card)
        if card:
            b = heapq.heappop(card)
            heapq.heappush(card, a + b)
            total += a + b

print(total)
