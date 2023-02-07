def slove(v, n, m):
    if v == m:
        a = ''
        for idx in range(len(ans)-1):
            a += str(ans[idx]) + ' '
            if ans[idx] > ans[idx+1]:
                return
        a += str(ans[len(ans)-1])
        if a not in s:
            print(a)
            s.add(a)
        return
    for i in range(n):
        if visited[i]:
            continue
        ans[v] = ns[i]
        visited[i] = True
        slove(v+1, n, m)
        visited[i] = False


n, m = map(int, input().split())
ns = sorted(list(map(int, input().split())))
ans = [0] * m
visited = [False] * n
s = set()
slove(0, n, m)