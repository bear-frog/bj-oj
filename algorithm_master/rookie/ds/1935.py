from collections import deque
deq = deque()
k = 65
n = int(input())
a = list(input())
for i in range(n):
    item = int(input())
    for idx in range(len(a)):
        if a[idx] == chr(k):
            a[idx] = item
    k += 1

for e in a:
    if e in ['+', '-', '*', '/']:
        i1 = deq.pop()
        i2 = deq.pop()
        res = eval(str(i2)+e+str(i1))
        deq.append(res)
    else:
        deq.append(e)

ans = float(deq.pop())
print(f"{ans:.2f}")
