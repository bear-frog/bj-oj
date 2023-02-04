def slove(count, sum, goal):
    if sum > goal:
        return False
    if sum == goal:
        return True
    now = 0
    for i in range(1, 4):
        now += slove(count + 1, sum + i, goal)
    return now


t = int(input())

for i in range(t):
    t = int(input())
    print(slove(0, 0, t))
