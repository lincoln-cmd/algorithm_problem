# codeforces 1676B

t = int(input())

for test in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    cnt = 0
    minimum = min(a)

    for i in a:
        cnt += (i - minimum)

    print(cnt)