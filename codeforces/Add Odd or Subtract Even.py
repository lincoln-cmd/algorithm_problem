t = int(input())

for test in range(t):
    a, b = map(int, input().split())
    
    c = b - a
    
    if c == 0:
        print(0)
    elif c > 0:
        if c % 2 == 0:
            print(2)
        else:
            print(1)
    else:
        if (c * -1) % 2 == 0:
            print(1)
        else:
            print(2)