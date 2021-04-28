data = list(map(int, input()))
mid = len(data) // 2
left = 0
right = 0
for i in data[:mid]:
    left += i
for i in data[mid:]:
    right += i

if left == right:
    print("LUCKY")
else:
    print("READY")
