t = int(input())

for i in range(t):
    k = int(input())
    
    cnt, x = 0, 0
    while cnt < k:
        x += 1
        if str(x)[-1] != '3' and x % 3 != 0:
            cnt += 1
        
    print(x)