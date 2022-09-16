t = int(input())

for test in range(t):
    num = str(input())
    
    first, last = num[:3], num[3:]
    
    a, b = 0, 0
    
    for i in range(3):
        a += int(first[i])
        b += int(last[i])
        
    if a == b:
        print('YES')
    else:
        print('NO')