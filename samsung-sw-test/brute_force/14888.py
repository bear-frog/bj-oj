import itertools

n = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))
arr = []
for idx in range(len(m)):
    if m[idx] == 0:
        continue
    if idx == 0:
        for i in range(m[idx]):
            arr.append(['+'])
    elif idx == 1:
        for i in range(m[idx]):
            arr.append(['-'] * m[idx])
    elif idx == 2:
        for i in range(m[idx]):
            arr.append(['*'] * m[idx])
    else:
        for i in range(m[idx]):
            arr.append(['/'] * m[idx])


mn = int(1e9)
mx = int(1e9) * -1

nPr = list(itertools.permutations(arr, n-1))
for p in nPr:
    v = a[0]
    i = 1
    for e in p:
        if e[0] == '+':
            v += a[i]
        elif e[0] == '-':
            v -= a[i]
        elif e[0] == '*':
            v *= a[i]
        elif e[0] == '/':
            if v < 0:
                v *= -1
                v //= a[i]
                v *= -1
            else:
                v //= a[i]
        i += 1
    mn = min(mn, v)
    mx = max(mx, v)

print(mx)
print(mn)