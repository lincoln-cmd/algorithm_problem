t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    cnt = 0
    
    for j in range(len(a)):
        a[j] = a[j] % 2
        
    if (len(a) % 2 == 0 and a.count(0) != a.count(1)) or ((len(a) % 2 == 1) and a.count(0) - 1 != a.count(1)):
        print(-1)
    else:    
        for j in range(len(a)):
            if j % 2 != a[j]:
                cnt += 1
        print(cnt // 2)