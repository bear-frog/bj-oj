word = list(input())
mp = [0] * 200

for w in word:
    mp[ord(w)] += 1

for i in range(97, 123):
    print(mp[i], end=' ')