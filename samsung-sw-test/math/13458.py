import math
n = int(input())
a = sorted(list(map(int, input().split())), reverse=False)
b, c = map(int, input().split())

ans = 0

for idx in range(len(a)):
    if a[idx] < 0:
        continue
    a[idx] -= b
    ans += 1

for idx in range(len(a)):
    if a[idx] < 0:
        continue
    ans += math.ceil(a[idx] / c)

print(ans)