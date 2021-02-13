import itertools
import copy


def print_graph(p_graph):
    for pi in range(n):
        for pj in range(n):
            print(p_graph[pi][pj], end=" ")
        print()


# 학생을 보면 True 리턴
def teacher_watching_bfs(t_graph, start, t_visited):
    tx, ty = start
    t_visited[tx][ty] = 1

    got_ya = 0
    for ii in range(4):
        xx = tx + dx[ii]
        yy = ty + dy[ii]
        while True:
            # 범위를 벗어나거나, 장애물을 만나면 전진을 멈춘다.
            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                break
            if t_graph[xx][yy] == "O" or t_graph[xx][yy] == "T":
                break

            # 이미 방문한 적이 있으면 continue
            if visited[xx][yy] == 1:
                # 현재 방향으로 계속 전진
                xx += dx[ii]
                yy += dy[ii]
                continue

            # 학생 발견
            if t_graph[xx][yy] == "S":
                got_ya += 1

            # 방문 처리
            t_visited[xx][yy] = 1
            # 현재 방향으로 계속 전진
            xx += dx[ii]
            yy += dy[ii]

    print("--------------got_ya=", got_ya, "명")
    print_graph(t_visited)
    print("--------------")

    return got_ya


n = int(input())
graph = []
blank_list = []
student_list = []
teacher_list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == "X":
            blank_list.append([i, j])
        elif graph[i][j] == "S":
            student_list.append([i, j])
        elif graph[i][j] == "T":
            teacher_list.append([i, j])

brute_case = [list(t) for t in itertools.combinations([i for i in range(len(blank_list))], 3)]

student_len = len(student_list)
safe_student = student_len
for case in brute_case:
    safe_student = student_len

    c_graph = copy.deepcopy(graph)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    # 장애물 세우기
    for c in case:
        c_graph[blank_list[c][0]][blank_list[c][1]] = "O"
        print(f"({blank_list[c][0]}, {blank_list[c][1]})", end=" ")
    print("장애물 설치")
    print(teacher_list, "선생님들")
    print_graph(c_graph)

    # 선생님들의 감시
    for t in teacher_list:
        print(t, "감시")
        # 학생을 발견하면 safe_student에서 제외
        safe_student -= teacher_watching_bfs(c_graph, t, visited)

    print("===================")
    print("===================")
    print("===================safe_student=", safe_student, "/", student_len)
    if safe_student == student_len:
        break

if safe_student == student_len:
    print("YES")
else:
    print("NO")
