def flip(l, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            l[i][j] = 1-l[i][j]


n, m = map(int, input().split())
l1 = [list(map(int, list(input()))) for _ in range(n)]
l2 = [list(map(int, list(input()))) for _ in range(n)]
ans = 0

for i in range(0, n-2):
    for j in range(0, m-2):
        if l1[i][j] != l2[i][j]:
            ans += 1
            flip(l1, i+1, j+1)

for i in range(0, n):
    for j in range(0, m):
        if l1[i][j] != l2[i][j]:
            print(-1)
            exit(0)

print(ans)
