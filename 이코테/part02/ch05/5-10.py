n, m = map(int, input().split())
data = []
count = 0


def dfs(_i, _j):
    if _i < 0 or _i >= n or _j < 0 or _j >= m:
        return False

    if data[_i][_j] == 0:
        data[_i][_j] = 1
        print(f"[{_i}, {_j}]", end=" ")
        dfs(_i - 1, _j)
        dfs(_i + 1, _j)
        dfs(_i, _j - 1)
        dfs(_i, _j + 1)
        return True
    else:
        return False


for i in range(n):
    data.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1
            print()

print(count)

"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

[의사코드]
def initial_graph(i,j,graph,data):
    global m,n
    if not (i-1<0 or i+1 == m or j-1<0 or j+1 == n):
        if data[i][j] ==0:
            graph[i].append([i,j])
        j += 1
        if (j == m):
            i +=1
        initial_graph(i,j,graph,data)
        
def initial_graph(_i, _j, _graph, _data):
    global m, n
    if _i < 0 or _i >= n or _j < 0 or _j >= m:
        return
    print("i:", _i, "j:", _j)

    if not visited[_i][_j]:
        visited[_i][_j] = True

        if _data[_i][_j] == 0:
            _graph[_i].append([_i, _j])

        initial_graph(_i - 1, _j, _graph, _data)
        initial_graph(_i + 1, _j, _graph, _data)
        initial_graph(_i, _j - 1, _graph, _data)
        initial_graph(_i, _j + 1, _graph, _data)
        

def initial_graph(_i, _j, _graph, _data, _count):
    global m, n
    if _i < 0 or _i >= n or _j < 0 or _j >= m:
        return

    print("i:", _i, "j:", _j, "count:", _count)
    if not visited[_i][_j]:
        visited[_i][_j] = True

        if _data[_i][_j] == 0:
            _graph[_i].append([_i, _j, _count])
        else:
            _j += 1
            if _j == m:
                _j = 0
                _i += 1

        initial_graph(_i - 1, _j, _graph, _data, _count)
        initial_graph(_i + 1, _j, _graph, _data, _count)
        initial_graph(_i, _j - 1, _graph, _data, _count)
        initial_graph(_i, _j + 1, _graph, _data, _count)
    else:
        return
"""
