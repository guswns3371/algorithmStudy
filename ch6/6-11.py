n = int(input())
lst = []
for _ in range(n):
    name, score = input().split()
    lst.append([name, int(score)])

lst = sorted(lst, key=lambda a: a[1])

for i in lst:
    print(i[0], end=" ")

