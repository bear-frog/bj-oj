min_value = int(1e9)
def dfs(depth, index):
    global min_value
    global graph
    if depth == n // 2:
        st = 0
        lk = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] and i != j and i > j:
                    st += graph[i][j] + graph[j][i]
                if not visited[i] and not visited[j] and i != j and i > j:
                    lk += graph[i][j] + graph[j][i]
        min_value = min(min_value, abs(st-lk))
        return depth

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

n = int(input())
visited = [False] * (n)
graph = [list(map(int, input().split())) for _ in range(n)]

dfs(0,0)

print(min_value)

# DFS(백트래킹)

def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)