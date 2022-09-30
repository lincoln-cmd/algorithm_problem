t = int(input())

for test in range(t):
    n, x = map(int, input().split())
    
    cnt = 2
    floor = 1
    
    while cnt < n:
        cnt += x
        floor += 1
        
    print(floor)