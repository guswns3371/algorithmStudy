import sys

input = sys.stdin.readline

n = int(input())
score = []

for _ in range(n):
    name, kor, eng, math = input().split()
    score.append((name, kor, eng, math))

result = sorted(score, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in result:
    print(s[0])
