t = int(input())

for test in range(t):
    s = list(map(int, input().split()))
    
    if max(s[0], s[1]) + max(s[2], s[3]) == sorted(s, reverse = True)[0] + sorted(s, reverse = True)[1]:
        print('YES')
    else:
        print('NO')