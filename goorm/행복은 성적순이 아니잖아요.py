t = int(input())

cnt = 0

for i in range(t):
    li = list(map(int, input().split()))
    
    l, s, n = li[0], li[1], li[2]
    
    k, m, v = li[3], li[4], li[5:]
    
    print((s / l) * 100, n)
    
    if (s / l) * 100 < n:
        for j in v:
            if j <= m:
                break
        else:
            cnt += 1
            
print(1 if cnt == t else 0)