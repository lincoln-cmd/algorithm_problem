t = int(input())

for test in range(t):
    s = str(input())
    
    if len(s) % 2 == 1:
        print('NO')
    else:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            print('YES')
        else:
            print('NO')