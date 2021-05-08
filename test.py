a = ['a', 'b', 'c', 'd', 'e']
print(a)
for i in range(5):
    print(f"a[{i}]={a[i]}")

for i in range(6):
    print(f"a[{-i}]={a[-i]}")

print("a[:5]", a[:5])
print("a[::]", a[::])
print("a[::-1]", a[::-1])
for i in range(5):
    print(f"a[ {i} : ] # {a[i:]}")
for i in range(1, 6):
    print(f"a[ {-i} : ] # {a[-i:]}")
print("a[ -4 : -1 ] # ",a[-4:-1])