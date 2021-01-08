from collections import deque

n = int(input())

# 진입차수
in_degrees = [0] * (n + 1)
# 강의 시간
times = [0] * (n + 1)
# 해당 강의를 수강하기 위해 들어야 할 최소 강의시간
tot_times = [0] * (n + 1)
# 위상 정렬 그래프
graph = [[] for i in range(n + 1)]

# 입력 받는 부분 : 강의시간 선수강의1 선수강의2 .. -1
for a in range(1, n + 1):
    input_lst = list(map(int, input().split()))
    # a번 강의의 강의시간을 times[a]에 입력
    times[a] = input_lst[0]
    tot_times[a] = input_lst[0]

    for b in range(1, len(input_lst)):
        if input_lst[b] != -1:
            # a번 강의는 선이수과목 input_lst[b]를 가진다 => 진입차수 = 선이수 과목 개수
            in_degrees[a] += 1
            # a번 강의 이수 후 들을 수 있는 과목 : input_lst[b]을 graph[a]에 덧붙힌다.
            graph[input_lst[b]].append(a)


def topology_sort():
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for d in range(1, len(in_degrees)):
        if in_degrees[d] == 0:
            q.append(d)
            continue

    while q:
        now = q.popleft()
        now_time = tot_times[now]
        # 현재 방문 노드 now 와 연결된 노드들은 g이다
        for g in graph[now]:
            if now_time + times[g] > tot_times[g]:
                tot_times[g] = now_time + times[g]
            # 연결된 노드의 진입차수 -1
            in_degrees[g] -= 1
            # 진입차수가 0 이면, 큐에다 해당 노드를 삽입
            if in_degrees[g] == 0:
                q.append(g)


topology_sort()

for i in range(1, len(tot_times)):
    print(tot_times[i])
