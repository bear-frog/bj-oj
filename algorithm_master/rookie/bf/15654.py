n, m = map(int, input().split())
ns = sorted(map(int, input().split()))
visited = [False] * 10001
ans = [0] * m
dict = {}
def slove(v, n, m):
    if v == m:
        t = ''
        tstr = ''
        tlst = []
        for i in range(m):
            t += str(ans[i]) + ' '
            tlst.append(str(ans[i]))
        tstr = "".join(sorted(tlst))
        if not dict.get(tstr):
            dict[tstr] = True
            print(t)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans[v] = ns[i]
        slove(v+1, n, m)
        visited[i] = False

slove(0,n,m)