# codeforces 1722A

t = int(input())

for test in range(t):
    n = int(input())
    s = list(str(input()))

    check = list('Timur')

    for i in range(len(check)):
        if check[i] in s:
            s.pop(s.index(check[i]))

    if len(s) == 0 and n == 5:
        print('YES')
    else:
        print('NO')
