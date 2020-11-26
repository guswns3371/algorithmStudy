n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
for i in lst:
    print(i, end=" ")
