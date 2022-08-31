t = int(input())

for test in range(t):
    d = list(map(int, input().split()))
    
    cnt = 0
    
    timur = d[0]
    
    for i in d[1:]:
        if i > timur:
            cnt += 1
            
    print(cnt)