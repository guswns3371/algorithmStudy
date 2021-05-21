from itertools import combinations
import copy


def gprint(data):
    for dd in data:
        for d in dd:
            print(d, end=" ")
        print()
    print()


n = int(input())
graph = []
teachers = []
students = []
blanks = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append([i, j])
        elif graph[i][j] == "S":
            students.append([i, j])
        elif graph[i][j] == "X":
            blanks.append([i, j])

cases = list(combinations(blanks, 3))
check = False
for case in cases:
    count = len(students)
    cgraph = copy.deepcopy(graph)
    for obj in case:
        cgraph[obj[0]][obj[1]] = "O"

    for teacher in teachers:
        tx, ty = teacher
        for i in range(4):
            xx, yy = tx, ty
            # 쭉 직진
            while True:
                xx += dx[i]
                yy += dy[i]
                # 맵을 벗어난 경우
                if xx < 0 or yy < 0 or xx >= n or yy >= n:
                    break
                # 장애물이 있는 곳
                if cgraph[xx][yy] == "O":
                    break
                # 다른 선생이 감시한 곳은 건너 뛴다
                if cgraph[xx][yy] == "T":
                    continue
                # 학생을 발견
                if cgraph[xx][yy] == "S":
                    count -= 1

                # 빈칸인 경우
                cgraph[xx][yy] = "T"

    print(case, count)
    gprint(cgraph)
    if count == len(students):
        check = True
        break

if check:
    print("YES")
else:
    print("NO")
