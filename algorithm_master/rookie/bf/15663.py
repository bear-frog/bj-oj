def slove(v, n, m):
    if v == m:
        a = ''
        for i in range(m):
            a += str(ans[i]) + ' '
        if not duplication.get(a):
            print(a)
            duplication[a] = True
        return
    for i in range(n):
        if visited[i]:
            continue
        ans[v] = ns[i]
        visited[i] = True
        slove(v + 1, n, m)
        visited[i] = False


n, m = map(int, input().split())
ns = sorted(list(map(int, input().split())))
visited = [False] * n
duplication = {}
ans = [0] * m

slove(0, n, m)
