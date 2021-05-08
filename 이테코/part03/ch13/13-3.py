from collections import deque


def bfs_spread_virus(graph, virus, visited):
    v_num, v_queue = virus
    print(v_num, "번 바이러스 : ", v_queue)
    t_queue = deque([])

    while v_queue:
        nx, ny = v_queue.popleft()

        print(v_num, "번 바이러스", nx, ny, "popleft")
        for d in range(4):
            xx = nx + dx[d]
            yy = ny + dy[d]
            print(xx, yy, end=" : ")
            # 지도를 벗어나는 경우, 방문했던 경우는 건너 뛴다.
            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                print("범위를 벗어남")
                continue

            if visited[xx][yy] == 1:
                print("이미감염")
                continue

            # 빈칸일 경우, 아직 방문하지 않은 칸인 경우만 바이러스 퍼뜨리기
            if graph[xx][yy] == 0 and visited[xx][yy] == 0:
                graph[xx][yy] = v_num
                print("감염", end=",")

                t_queue.append([xx, yy])
                print("방문처리!")
                visited[xx][yy] = 1
        print()

    while t_queue:
        tx, ty = t_queue.popleft()
        v_queue.append([tx, ty])

    print(v_queue)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
infected = []
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))
    # 바이러스가 감연된 위치를 infected 리스트에 넣는다
    for j in range(n):
        if graph[i][j] != 0:
            # infected 리스트 원소 형식 : 바이러스 번호, deque([[바이러스 x좌표,y좌표]])
            infected.append([graph[i][j], deque([[i, j]])])
            # 방문처리
            visited[i][j] = 1

# s초 뒤에 (x,y)에 존재하는 바이러스의 종류
s, x, y = map(int, input().split())

# 바이러스 번호 기준으로 infected 리스트 정렬
infected.sort()
print(infected)
for i in range(s):
    for virus in infected:
        virus_num, queue = virus
        bfs_spread_virus(graph, virus, visited)

        print("------------------", i + 1, "초", virus_num, "번 바이러스")
        for a in range(n):
            for b in range(n):
                print(graph[a][b], end=" ")
            print()
        print("방문기록")
        for a in range(n):
            for b in range(n):
                print(visited[a][b], end=" ")
            print()
        print("------------------------------------")
        print()
        print()

    # 바이러스가 모두 퍼졌다면 반복문을 끝낸다 : 시간초과 발생하기 때문
    flag = True
    for a in range(n):
        for b in range(n):
            if visited[a][b] == 0:
                flag = False
    if flag:
        break


# 결과
print(graph[x - 1][y - 1])

'''
1 1
1
2 1 1

3 3
1 0 2
0 0 0
3 0 0
2 3 2

5 3
1 0 2 0 0
0 0 0 0 0
3 0 0 0 1
0 0 0 0 0
1 0 0 0 0
10 3 2
'''
