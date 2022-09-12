t = int(input())

for test in range(t):
    h, m = map(int, input().split())
    
    if m == 0:
        print((24 - h) * 60)
    else:
        print((23 - h) * 60 + (60 - m))