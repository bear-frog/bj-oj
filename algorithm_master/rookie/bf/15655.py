n, m = map(int, input().split())
ns = sorted(map(int, input().split()))
visited = [False] * n
ans = [0] * m

def slove(v, n, m):
    if v == m:
        print(ans[:m])
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans[v] = ns[i]
        slove(v+1, n, m)
        visited[i] = False

slove(0,n,m)