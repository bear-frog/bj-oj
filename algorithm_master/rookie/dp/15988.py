mx = 1000001
n = 1000000009
d = [0] * mx

d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(4, mx):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % n

cnt = int(input())
for _n in range(cnt):
    print(d[int(input())])