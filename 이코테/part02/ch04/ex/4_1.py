n = int(input())
plan = input().split()

col = 1
row = 1

for go in plan:
    if go == 'L':
        if col == 1:
            continue
        col -= 1
    elif go == "R":
        if row == n:
            continue
        col += 1
    elif go == "U":
        if row == 1:
            continue
        row -= 1
    else:  # D
        if row == n:
            continue
        row += 1

print(row, col)
"""
5
R R R U D D
"""
