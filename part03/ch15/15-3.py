def binary_search_share(array, visited, result, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    d, e, f = array[start], array[mid], array[end]


n, c = map(int, input().split())
house = []
result = []
visited = [0] * n
for _ in range(n):
    house.append(int(input()))

house.sort()
