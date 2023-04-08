# codeforces 1462-A

t = int(input())

for test in range(t):
    n = int(input())

    b = list(map(int, input().split()))

    li = []

    for i in range(n):
        if i % 2 == 0:
            li.append(b.pop(0))
        else:
            li.append(b.pop())

    print(*li)