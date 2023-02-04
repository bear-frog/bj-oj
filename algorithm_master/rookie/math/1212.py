n = list(input())
ans = ''

for e in n:
    temp = int(e)
    while temp != 0:
        if temp % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        temp //= 2

print(ans)