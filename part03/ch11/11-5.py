n, m = map(int, input().split())
m_list = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i + 1, n):
        if m_list[i] != m_list[j]:
            count += 1

print(count)
