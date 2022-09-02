t = int(input())

for test in range(t):
    w, h, n = map(int, input().split())
    cnt = 0
    
    while True:
        if w % 2 == 0:
            w //= 2
            cnt += 1
        elif h % 2 == 0:
            h //= 2
            cnt += 1
        else:
            break
    
    print('yes' if 2**cnt >= n else 'no')