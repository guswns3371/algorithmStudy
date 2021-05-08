import sys

input = sys.stdin.readline

n = int(input())

houses = list(map(int, input().split()))
houses.sort()

if n % 2 == 1:
    print(houses[len(houses) // 2])
else:
    print(houses[len(houses) // 2 - 1])
