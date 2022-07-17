t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if min(a) >= max(b):
        print(sum(a))
    else:
        while k:
            a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
            k -= 1
            if min(a) >= max(b):
                break
        print(sum(a))