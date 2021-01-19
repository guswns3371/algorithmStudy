n = list(map(int,input()))
count = 0
print("i", "n[i]", "n[i+1]", "count", "문자열")
for i in range(len(n)):
    if i < len(n) - 1:
        if n[i] != n[i + 1]:
            # n[i + 1].replace(n[i + 1], n[i])
            n[i + 1] = n[i]
            count += 1

    else:
        break
print(int(count))  # 왜냐면 다른 부분은 앞 뒤로 있으므로...?
