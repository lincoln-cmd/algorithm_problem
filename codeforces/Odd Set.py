# codeforces 1542A

t = int(input())

for test in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    cnt = 0

    for i in a:
        if i % 2 == 0:
            cnt += 1

    if cnt == n:
        print('Yes')
    else:
        print('No')