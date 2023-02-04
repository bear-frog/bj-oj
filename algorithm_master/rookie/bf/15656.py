def slove(v, n, m):
    if v == m:
        for i in range(m):
            print(ans[i],end=' ')
        print()
        return
    for i in range(n):
        # if visited[i]:
        #     continue
        ans[v] = ns[i]
        # visited[i] = True
        slove(v + 1, n, m)
        # visited[i] = False


n, m = map(int, input().split())
ns = sorted(list(map(int, input().split())))
# visited = [False] * n
ans = [0] * m

slove(0, n, m)
