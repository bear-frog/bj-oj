def slove(v, n, m):
    if v == m:
        a = ''
        for idx in range(len(ans)-1):
            if ans[idx] > ans[idx+1]:
                return
            else:
                a += str(ans[idx]) + ' '
        a += str(ans[len(ans)-1])
        print(a)
        return
    for i in range(n):
        ans[v] = ns[i]
        # visited[i] = True
        slove(v+1, n, m)
        # visited[i] = False


n, m = map(int, input().split())
ns = sorted(list(map(int, input().split())))
ans = [0] * m
# visited = [False] * n
slove(0, n, m)