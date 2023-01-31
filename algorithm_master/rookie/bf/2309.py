from itertools import permutations

a = []
s = 0
for i in range(9):
    a.append(int(input()))

a = sorted(a)
s = sum(a)
perm = list(permutations(a, 2))

for e in perm:
    if s - (e[0] + e[1]) == 100:
        a.remove(e[0])
        a.remove(e[1])
        break

for e in a:
    print(e)