t = int(input())

for test in range(t):
    x = int(input())
    
    a, b = str(x)[0], len(str(x))
    length = [1, 2 ,3, 4]
    
    print((int(a) - 1) * 10 + sum(length[:b]))