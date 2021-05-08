def dfs(_graph, v, _visited):
    _visited[v] = True
    print(v, end=" ")
    for i in _graph[v]:
        if not _visited[i]:
            dfs(_graph, i, _visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
