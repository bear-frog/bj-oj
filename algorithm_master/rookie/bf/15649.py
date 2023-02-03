n, m = map(int, input().split())
visited = [False] * 10
ans = [0] * 10

def slove(v, n, m):
    if v == m:
        for i in range(m):
            print(ans[i],end=' ')
        print()
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans[v] = i + 1
        slove(v + 1, n, m)
        visited[i] = False


slove(0, n, m)

# import sys
# n,m = map(int,input().split())
# c = [False]*(n+1)
# a = [0]*m
#
# def go(index, n, m):
#     if index == m:
#         sys.stdout.write(' '.join(map(str,a))+'\n')
#         return
#     for i in range(1, n+1):
#         if c[i]:
#             continue
#         c[i] = True
#         a[index] = i
#         go(index+1, n, m)
#         c[i] = False
#
# go(0,n,m)